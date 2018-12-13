SERIAL_NUMBER = 5034
GRID_SIZE = 300
GRID_SIZE += 1

def power_level(x, y):
    rack_id = x+10
    power_level = rack_id*y
    power_level += SERIAL_NUMBER
    power_level = power_level * rack_id
    try:
        power_level = int(str(power_level)[-3])
    except IndexError:
        power_level = 0
    return power_level - 5

#output = ''
power = {}
for x in range(1, GRID_SIZE+1):
    for y in range(1, GRID_SIZE+1):
        power[(x, y)] = power_level(x, y)
#        output += str(power[(x,y)]).center(4)
#    output += '\n'

#print(output)

best_cell = (0, 0, 0)
best_power = 0

for x in range(1, GRID_SIZE):
    for y in range(1, GRID_SIZE):
        test_power = 0
        #test_includes = []
        for size in range(GRID_SIZE-max(x, y)):
            #print(x, y, size+1)
            new_column_x = x+size
            for new_column_y in range(y, y+size+1):
                test_power += power[(new_column_x, new_column_y)]
                #test_includes.append((new_column_x, new_column_y))

            for new_row_x in range(x, x+size):
                test_power += power[(new_row_x, new_column_y)]
                #test_includes.append((new_row_x, new_column_y))

            #print(test_includes, test_power)
            if test_power > best_power:
                best_cell = (x, y, size+1)
                best_power = test_power

print('The best',best_cell[2],'x',best_cell[2],'square has the top left fuel cell of', (best_cell[0],best_cell[1]), 'with', best_power, 'power')
