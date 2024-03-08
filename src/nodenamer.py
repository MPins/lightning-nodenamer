import sys 
import ijson

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
            # Check if the resulting list has exactly two pieces
            if len(pieces) == 2: self.data = {}
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
            # Check if the resulting list has exactly two pieces
            if len(pieces) == 2: self.data = {}            
            return False
        elif self.state == 'map_ended' and event == 'map_key':
            print("Transitioning from 'map_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_ended' and event == 'end_map':
            print("Transitioning from 'map_ended' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            pieces = prefix.split('.')
            # Check if the resulting list has exactly two pieces
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

    # Create an instance of the state machine
    sm = state_machine()

    # Open the JSON file for reading
    with open(json_file, 'r') as file:
        # Create an iterator for the JSON data
        parser = ijson.parse(file)
    
        # Iterate over each JSON event
        for prefix, event, value in parser:
            # Perform transitions
            sm.event(event, prefix, value)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nodenamer.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    main(json_file)

