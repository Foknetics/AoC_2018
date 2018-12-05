with open('input.txt') as file:
    data = file.read()

fabric = {}
for claim in data.splitlines():
    claim_data = claim.split()
    _id = claim_data[0][1:]
    x_pos = int(claim_data[2].split(',')[0])
    y_pos = int(claim_data[2].split(',')[1][:-1])
    width = int(claim_data[3].split('x')[0])
    height = int(claim_data[3].split('x')[1])

    for x_inch in range(width):
        for y_inch in range(height):
            new_cords = (x_pos+x_inch, y_pos+y_inch)
            try:
                fabric[new_cords].append(_id)
            except KeyError:
                fabric[new_cords] = [_id]

#fabric_string = ''
#for y in range(8):
#    for x in range(8):
#        if (x, y) in fabric:
#            if len(fabric[(x, y)]) > 1:
#                fabric_string += 'X'
#            else:
#                fabric_string += str(fabric[(x, y)][0])
#        else:
#            fabric_string += '.'
#    fabric_string += '\n'
#
#print(fabric_string)

count = 0
for key in fabric.keys():
    if len(fabric[key]) > 1:
        count += 1

print(count, 'inches of fabric are within two or more claims')
