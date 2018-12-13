def power_level(x, y):
    serial_number = 5034
    rack_id = x+10
    power_level = rack_id*y
    power_level += serial_number
    power_level = power_level * rack_id
    try:
        power_level = int(str(power_level)[-3])
    except IndexError:
        power_level = 0
    return power_level - 5

best_cell = (0, 0)
best_power = 0
for x in range(1, 299):
    for y in range(1, 299):
        total = power_level(x,y) + power_level(x+1, y) + power_level(x+2, y) + \
                power_level(x,y+1) + power_level(x+1, y+1) + power_level(x+2, y+1) + \
                power_level(x,y+2) + power_level(x+1, y+2) + power_level(x+2, y+2)
        if total > best_power:
            best_cell = (x, y)
            best_power = total

print('The best 3x3 square has the top left fuel cell of', best_cell, 'with', best_power, 'power')