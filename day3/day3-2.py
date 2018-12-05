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

def check_claim(claim_data):
    _id = claim_data[0][1:]
    x_pos = int(claim_data[2].split(',')[0])
    y_pos = int(claim_data[2].split(',')[1][:-1])
    width = int(claim_data[3].split('x')[0])
    height = int(claim_data[3].split('x')[1])

    for x_inch in range(width):
        for y_inch in range(height):
            new_cords = (x_pos+x_inch, y_pos+y_inch)
            if fabric[new_cords] != [_id]:
                return False
    return True


for claim in data.splitlines():
    claim_data = claim.split()
    if check_claim(claim_data):
        print('Claim', claim_data[0][1:], 'has no overlapping claims')
        break
