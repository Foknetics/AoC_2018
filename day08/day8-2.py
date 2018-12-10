with open('input.txt') as file:
    data = file.read()

numbers = data.split(' ')
#current_id = 65

def node_value(node):
    if node['number_of_children'] == 0:
        return sum(node['metadata'])
    else:
        value = 0
        for metadata in node['metadata']:
            if metadata == 0:
                continue
            else:
                try:
                    value += node_value(node['children'][metadata-1])
                except IndexError:
                    continue
        return value

def process_node(numbers):
    #global current_id
    node = {#'id': chr(current_id),
            'number_of_children': int(numbers.pop(0)),
            'children': [],
            'number_of_metadata': int(numbers.pop(0)),
            'metadata':[]}
    current_id += 1
    for x in range(node['number_of_children']):
        node['children'].append(process_node(numbers))
    for x in range(node['number_of_metadata']):
        node['metadata'].append(int(numbers.pop(0)))
    node['value'] = node_value(node)
    return node

root = process_node(numbers)
#import json
#print(json.dumps(root, indent=2))
print('The value of the root node is', root['value'])
