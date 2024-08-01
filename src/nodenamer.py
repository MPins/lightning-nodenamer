import sys 
import ijson
import re
import os
import datetime
import json
from collections import Counter

# The definition of the finger print using the feature bits
from feature_bits_templates import bolt9_feature_flags, templates_index, templates_list

# This function receives input JSON file and create the new output JSON file 
# without the alias field.
# Sometimes the field ends on the next line with the comma (,)
# When it happens it will be deleted also
def remove_alias(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            alias = False
            for line in f_in:
                if alias == True:
                    alias = False
                    if ',' in line:
                        continue
                if not re.search(r'"alias"', line):
                    f_out.write(line)
                else:
                    if ',' not in line:
                        alias = True

# Using the color it is not that hard information, but we use it as 3th layer
def implementation_by_color(color):
    if color == "#3399ff":
        return 'LND'
    elif color == "#49daaa":
        return 'ECLR'
    else:
        return 'UNKNOWN'

# Function to check if feature exists in the list
def feature_exists(feature, features_list):
    for existing_feature in features_list:
        if all(existing_feature[key] == feature[key] for key in feature):
            existing_feature['qty'] += 1
            return True
    return False

# Feature bits class
class feature_bits:
    def __init__(self):
        self.count = []
        self.log = []

    def counter(self, data, pubkey):
        # Accessing the features
        for key, value in data.items():
            # Splitting the key to extract information
            parts = key.split('.')

            if parts[4] == 'name':

                # It will take the name of the flag from the bolt 9 spec
                # If it is not found it will assume the one received on json file
                for flag in bolt9_feature_flags:
                    if flag.get(parts[3]):
                        flag_name = flag[parts[3]]
                        break
                    else:
                        flag_name = value

                current_feature = {'feature_bit': parts[3], 'feature_name': flag_name}
                
            elif parts[4] == 'is_required':
                current_feature['is_required'] = value

            elif parts[4] == 'is_known':
                current_feature['is_known'] = value
                if feature_exists(current_feature, self.count) is False:
                    current_feature['qty'] = 1
                    self.count.append(current_feature)
                # Insert the node id at the starting of current_feature
                # Insert the new key-value pair at the beginning of the dictionary
                current_feature = {'nodeid': pubkey, **current_feature}
                self.log.append (current_feature)
                
            else:
                # Raise a exception
                raise Exception("Error on feature bits counter.")


# State machine class
class state_machine:
    def __init__(self):
        self.state = 'initial'

    def event(self, event, prefix, data):

        if self.state == 'initial' and event == 'start_map':
            # print("Transitioning from 'initial' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            return False
        elif self.state == 'map_started' and event == 'map_key':
            # print("Transitioning from 'map_started' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_started' and event == 'end_map':
            # print("Transitioning from 'map_started' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            return False
        elif self.state == 'mapping' and event == 'start_map':
            # print("Transitioning from 'mapping' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            return False
        elif self.state == 'mapping' and event == 'start_array':
            # print("Transitioning from 'mapping' to 'array_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_started'
            return False
        elif self.state == 'mapping' and event == 'null':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = ""
            return False
        elif self.state == 'mapping' and event == 'number':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'mapping' and event == 'string':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'mapping' and event == 'boolean':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'array_started' and event == 'start_map':
            # print("Transitioning from 'array_started' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'           
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we initate the data field with nodes or edges
            if len(pieces) == 2: self.data = {"data_type":pieces[0]}
            return False 
        elif self.state == 'array_started' and event == 'end_array':
            # print("Transitioning from 'array_started' to 'array_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_ended'
            return False
        elif self.state == 'mapped' and event == 'map_key':
            # print("Transitioning from 'mapped' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'mapped' and event == 'end_map':
            # print("Transitioning from 'mapped' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            return False
        elif self.state == 'map_ended' and event == 'end_array':
            # print("Transitioning from 'map_ended' to 'array_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_ended'
            return False
        elif self.state == 'map_ended' and event == 'start_map':
            # print("Transitioning from 'map_ended' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we initate the data field
            if len(pieces) == 2: self.data = {"data_type":pieces[0]}            
            return False
        elif self.state == 'map_ended' and event == 'map_key':
            # print("Transitioning from 'map_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_ended' and event == 'end_map':
            # print("Transitioning from 'map_ended' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we return true.
            # This way the calling function know that the data field must be used 
            # imeddiatelly, because he might be initialised during the forward interactions
            if len(pieces) == 2: return True
        elif self.state == 'array_ended' and event == 'map_key':
            # print("Transitioning from 'array_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'array_ended' and event == 'end_map':
            # print("Transitioning from 'array_ended' to 'final' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'final'
            return False
        else:
            print("Invalid transition")

# Process the json file generated by the lncli describegraph 
def main(json_file):
    try:
        # Initialize the output lists
        output = []
        output_temp = []
        output_unknown = []
        output_no_features = []
        output_no_updates = []
        output_no_features_temp = []
        output_no_updates_temp = []
        list_of_unknown_fingerprint = []
        final_list_of_unknown_fingerprint = []
        counter_of_unknown_fingerprint = []
        
        #Initialize counters
        counters = {'LND': 0, 'CLN': 0, 'ECLR': 0,'LDK': 0,'UNKNOWN': 0,'NOFEATURES': 0,'NOUPDATE': 0}
        nodes_counter = 0
        channels_counter = 0

        # intialize the counters where the node is identified
        counter_feature_bits = 0
        counter_channel_policy = 0
        counter_color = 0

        # Create an instance of the state machine
        sm = state_machine()

        # Create an instance of the feature bits class to create feature bits statistics
        fb = feature_bits()

        # Open the JSON file for reading
        with open(json_file, 'r', encoding='utf-8', errors='ignore') as file:
            try:
                parser = ijson.parse(file)  # Create an iterator for the JSON data
                for prefix, event, value in parser:
                    # Process the JSON events as needed
                    # Perform transitions
                    # If the transition results in completed nodes or edges data
                    # Takes the data to mount the output
                    if sm.event(event, prefix, value) is True:
                        if sm.data['data_type'] == "nodes":
                            nodes_counter +=1
                            del sm.data['data_type']
                            pubkey = sm.data['nodes.item.pub_key']
                            node_color = sm.data['nodes.item.color']
                            last_update = sm.data['nodes.item.last_update']
                            # deleting data to compare the features fingerprint only
                            for key, value in sm.data.copy().items():
                                # Process the key-value pair
                                pieces = key.split('.')
                                if pieces[2] != "features" and len(pieces) > 2:
                                    del sm.data[key]

                            # count the feature bits
                            fb.counter(sm.data, pubkey)

                            template_found = False
                            # ***** FIRST LAYER ***** trying to identify the node using the feature bits
                            for i, template in enumerate(templates_list):
                                if template == sm.data:
                                    template_found = True
                                    # Extract implementation and version from the template index
                                    templates_index[i]['Qty'] += 1
                                    new_output = {"id": pubkey, "implementation": templates_index[i]['implementation'], "version": templates_index[i]['version']}
                                    output.append(new_output)
                                    counter_feature_bits += 1
                            
                            # If not found a template of features bits inserting this node as UNKOWN
                            # We are going to figure out the node implementation using the channel default policies
                            # And the default color captured above
                            if template_found == False and last_update != 0 and len(sm.data) > 0:
                                templates_index[len(templates_index)-3]['Qty'] += 1
                                new_output = {"id": pubkey, "color": node_color, "implementation": "UNKNOWN", "version": "UNKNOWN", 'LND': 0, 'LDK': 0, 'CLN': 0, 'ECLR': 0}
                                output_temp.append(new_output)
                            if template_found == False and last_update != 0 and len(sm.data) == 0:
                                templates_index[len(templates_index)-2]['Qty'] += 1
                                new_output = {"id": pubkey, "color": node_color, "implementation": "NOFEATURES", "version": "NOFEATURES", 'LND': 0, 'LDK': 0, 'CLN': 0, 'ECLR': 0}
                                output_no_features_temp.append(new_output)                    
                            if template_found == False and last_update == 0:
                                templates_index[len(templates_index)-1]['Qty'] += 1
                                new_output = {"id": pubkey, "color": node_color, "implementation": "NOUPDATE", "version": "NOUPDATE", 'LND': 0, 'LDK': 0, 'CLN': 0, 'ECLR': 0}
                                output_no_updates_temp.append(new_output)

                            # Storing the features fingerprints that was not found on the templates

                            if template_found == False and sm.data != {}:
                                list_of_unknown_fingerprint.append(sm.data)
                                
                        # ***** SECOND LAYER ***** trying to identify the node using the defaul channel policies (continue)         
                        elif sm.data['data_type'] == "edges":
                            channels_counter += 1
                            if sm.data['edges.item.last_update'] == 0: continue
                            # I'm counting the each distribution time_lock_delta default of each channel of the nodes
                            # that based on feature bits are unkown
                            for node in output_temp:
                                if node.get('id') == sm.data['edges.item.node1_pub'] and node.get('implementation') == 'UNKNOWN':
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 144:
                                        node['ECLR'] +=1
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 72:
                                        node['LDK'] +=1
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 6:
                                        node['CLN'] +=1
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 40 or sm.data.get('edges.item.node1_policy.time_lock_delta') == 80:
                                        node['LND'] +=1
                                if node.get('id') == sm.data['edges.item.node2_pub'] and node.get('implementation') == 'UNKNOWN':
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 144:
                                        node['ECLR'] +=1
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 72:
                                        node['LDK'] +=1
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 6:
                                        node['CLN'] +=1
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 40 or sm.data.get('edges.item.node2_policy.time_lock_delta') == 80:
                                        node['LND'] +=1
                        print(f"Nodes: {nodes_counter} | Channels: {channels_counter}", end="\r")    
                                         
            except ijson.JSONError as e:
                print(f"Error parsing JSON: {e}")                

        for i in range(len(list_of_unknown_fingerprint)):
            if list_of_unknown_fingerprint[i] not in final_list_of_unknown_fingerprint:
                final_list_of_unknown_fingerprint.append(list_of_unknown_fingerprint[i]) 
                counter_of_unknown_fingerprint.append(list_of_unknown_fingerprint.count(list_of_unknown_fingerprint[i]))


        print()

        # ***** SECOND LAYER ***** trying to identify the node using the defaul channel policies
        # Take the nodes data stored on output_unknown and use it to try identifying them
        output_temp.extend(output_no_features_temp)
        output_temp.extend(output_no_updates_temp)
        for node in output_temp:
            max_value = 0
            max_key = 'LND'
            for key in ['LND', 'CLN', 'ECLR', 'LDK']:
            # Update max_key and max_value if the current value is greater
                if node[key] > max_value:
                    max_key = key
            if node[max_key] > 0:
                new_output = {"id": node['id'], "implementation": max_key, "version": 'UNKNOWN'}
                output.append(new_output)
                counter_channel_policy += 1
            else:
                # ***** THIRD LAYER ***** trying to identify the node using the defaul node color
                imp_by_color = implementation_by_color(node['color'])
                if imp_by_color == "UNKNOWN":
                    if node['implementation'] == "UNKNOWN": 
                        new_output = {"id": node['id'], "implementation": "UNKNOWN", "version": 'UNKNOWN'}
                        output_unknown.append(new_output)   
                    elif node['implementation'] == "NOFEATURES":
                        new_output = {"id": node['id'], "implementation": "NOFEATURES", "version": 'UNKNOWN'}
                        output_no_features.append(new_output)
                    elif node['implementation'] == "NOUPDATE":
                        new_output = {"id": node['id'], "implementation": "NOUPDATE", "version": 'UNKNOWN'}
                        output_no_updates.append(new_output)
                else:
                        new_output = {"id": node['id'], "implementation": imp_by_color, "version": 'UNKNOWN'}
                        output.append(new_output)
                        counter_color += 1

        with open('nodenamer.log', 'a', encoding='utf-8') as f_out:
            for node_list in [output, output_unknown, output_no_updates, output_no_features]:
                for node in node_list:
                    current_datetime = datetime.datetime.now()
                    datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
                    key = node.get('implementation')
                    counters[key] += 1            
                    line = datetime_string + " " + "IMPLEMENTATION=" + node.get('implementation') + " " + "VERSION=" + node.get('version') + " " + "ID=" + node.get('id') + "\n"
                    f_out.write(line)
                 
        for label, qty in counters.items():
            print(f"{label}: {qty}")

        # Order features_list by feature_bit
        ordered_features = sorted(fb.count, key=lambda x: int(x['feature_bit']))

        # Function to print each item of the features bit list
        with open('nodenamer-features-total.log', 'a', encoding='utf-8') as f_out:
            for feature in ordered_features:                
                current_datetime = datetime.datetime.now()
                datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
                line = datetime_string
                for key, value in feature.items():
                    print(f"{key}={value} ", end=" ")
                    line = line + " " + key + "=" + str(value)
                line = line + "\n"
                f_out.write(line)
                print()  # Move to the next line after printing all attributes of the item

        print(f"Nodes identified by Feature Bits = {counter_feature_bits}, Channels Policy = {counter_channel_policy}, Color = {counter_color}")

        with open('nodenamer-features.log', 'a', encoding='utf-8') as f_out:
            for feature_log in fb.log:
                current_datetime = datetime.datetime.now()
                datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
                line = datetime_string + " nodeid=" + feature_log['nodeid'] + " feature_bit=" + feature_log['feature_bit'] + " feature_name=" + feature_log['feature_name'] + "\n" 
                f_out.write(line)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nodenamer.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]

    # create another file ignoring the alias field due the erros it cause whe parsing it
    # because of unexpected characteres
    file_name, file_extension = os.path.splitext(json_file)

    s_json_file = file_name + "_s" + file_extension
    remove_alias(json_file, s_json_file)
        
    main(s_json_file)

    # delete the created file
    if os.path.exists(s_json_file):
        # Delete the file
        os.remove(s_json_file)

