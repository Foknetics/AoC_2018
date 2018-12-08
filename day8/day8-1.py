with open('input.txt') as file:
    data = file.read()

numbers = data.split(' ')

nodes=[]
def process_node(numbers):
    node = {'number_of_children': int(numbers.pop(0)),
            'number_of_metadata': int(numbers.pop(0)),
            'metadata':0}
    nodes.append(node)
    for x in range(node['number_of_children']):
        process_node(numbers)
    for x in range(node['number_of_metadata']):
        node['metadata'] += int(numbers.pop(0))
    return nodes

nodes = process_node(numbers)
total_meta = 0
for node in nodes:
    total_meta += node['metadata']

print('The sum of all metadata is', total_meta)
