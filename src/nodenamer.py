import sys 
import ijson

# Feature bits templates 
templates_index = [
                    {'CLN': 'v23.05.2','Qty': 0},
                    {'ECLR': 'v0.9.0 or v0.8.0','Qty': 0},
                    {'LND': 'UNKOWN','Qty': 0},
                    {'LDK': 'v.0.1.0', 'Qty': 0},
                    {'CLN': 'v.23.0.2 or v0.12.0', 'Qty': 0},
                    {'ECLR': 'v0.7.0', 'Qty': 0},
                    {'UNKNOWN': 'UNKOWN','Qty': 0}
                   ]
templates_list = [
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.39.name': 'unknown', 'nodes.item.features.39.is_required': False, 'nodes.item.features.39.is_known': False,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True,  'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.39.name': 'unknown', 'nodes.item.features.39.is_required': False, 'nodes.item.features.39.is_known': False,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.39.name': 'unknown', 'nodes.item.features.39.is_required': False, 'nodes.item.features.39.is_known': False,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True
                    }
]

# State machine class
class state_machine:
    def __init__(self):
        self.state = 'initial'

    def event(self, event, prefix, data):

        if self.state == 'initial' and event == 'start_map':
            print("Transitioning from 'initial' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            return False
        elif self.state == 'map_started' and event == 'map_key':
            print("Transitioning from 'map_started' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_started' and event == 'end_map':
            print("Transitioning from 'map_started' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            return False
        elif self.state == 'mapping' and event == 'start_map':
            print("Transitioning from 'mapping' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            return False
        elif self.state == 'mapping' and event == 'start_array':
            print("Transitioning from 'mapping' to 'array_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_started'
            return False
        elif self.state == 'mapping' and event == 'number':
            print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'mapping' and event == 'string':
            print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'mapping' and event == 'boolean':
            print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'array_started' and event == 'start_map':
            print("Transitioning from 'array_started' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'           
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we initate the data field
            if len(pieces) == 2: self.data = {"data_type":pieces[0]}
            return False 
        elif self.state == 'array_started' and event == 'end_array':
            print("Transitioning from 'array_started' to 'array_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_ended'
            return False
        elif self.state == 'mapped' and event == 'map_key':
            print("Transitioning from 'mapped' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'mapped' and event == 'end_map':
            print("Transitioning from 'mapped' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            return False
        elif self.state == 'map_ended' and event == 'end_array':
            print("Transitioning from 'map_ended' to 'array_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_ended'
            return False
        elif self.state == 'map_ended' and event == 'start_map':
            print("Transitioning from 'map_ended' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we initate the data field
            if len(pieces) == 2: self.data = {"data_type":pieces[0]}            
            return False
        elif self.state == 'map_ended' and event == 'map_key':
            print("Transitioning from 'map_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_ended' and event == 'end_map':
            print("Transitioning from 'map_ended' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we return true.
            # This way the calling function know that the data field must be used 
            # imeddiatelly, because he might be initialised during the forward interactions
            if len(pieces) == 2: return True
        elif self.state == 'array_ended' and event == 'map_key':
            print("Transitioning from 'array_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'array_ended' and event == 'end_map':
            print("Transitioning from 'array_ended' to 'final' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'final'
            return False
        else:
            print("Invalid transition")

# Process the json file generated by the lncli describegraph 
def main(json_file):

    # Initialize the output list
    output = []

    # Create an instance of the state machine
    sm = state_machine()

    # Open the JSON file for reading
    with open(json_file, 'r') as file:
        # Create an iterator for the JSON data
        parser = ijson.parse(file)
    
        # Iterate over each JSON event
        for prefix, event, value in parser:
            # Perform transitions
            # If the transition results in completed nodes or edges data
            # Takes the data to mount the output
            if sm.event(event, prefix, value) is True:
                if sm.data['data_type'] == "nodes":
                    del sm.data['data_type']
                    pubkey = sm.data['nodes.item.pub_key']
                    color = sm.data['nodes.item.color']
                    # deleting data to compare the features fingerprint only
                    # Remove the key-value pair with key "age"
                    for key, value in sm.data.copy().items():
                        # Process the key-value pair
                        pieces = key.split('.')
                        if pieces[2] != "features":
                            del sm.data[key]

                    template_found = False
                    for i, template in enumerate(templates_list):
                        if template == sm.data:
                            template_found = True
                            # Extract distribution and version from the template index
                            dist_version = templates_index[i]
                            templates_index[i]['Qty'] += 1
                            for dist, version in dist_version.items():
                                new_output = {"id": pubkey, "implementation": dist, "version": version}
                                output.append(new_output)
                    
                    # If not found a template of features bits inserting this node as UNKOWN
                    # We are going to figure out the node implementation using the channel default policies
                    # And the default color captured above
                    if template_found != True:
                        templates_index[len(templates_index)-1]['Qty'] += 1
                        new_output = {"id": pubkey, "implementation": "UNKOWN", "version": "UNKOWN"}
                        output.append(new_output)
        
        
        # Sort the template index based on the qty
        sorted_list = sorted(templates_index, key=lambda x: x["Qty"], reverse=True)
        for dictionary in sorted_list:
            for key, value in dictionary.items():
                print(f"{key}: {value}", end=" ")  # Print key-value pair on the same line
            print()  # Move to the next line after printing all key-value pairs for the current dictionary

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nodenamer.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    main(json_file)

