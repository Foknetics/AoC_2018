def map_print(cave_map, units):
    max_x = sorted([x[0] for x in cave_map], reverse=True)[0]+1
    max_y = sorted([x[1] for x in cave_map], reverse=True)[0]+1
    living_units = [x for x in units if x['hp'] > 0]
    unit_locations = [x['location'] for x in living_units]
    output = ' '+''.join([str(x)[-1] for x in range(max_x)])+'\n'
    for y in range(max_y):
        output += str(y)
        for x in range(max_x):
            if (x,y) in unit_locations:
                output += living_units[unit_locations.index((x,y))]['type']
            else:
                output += cave_map[(x,y)]
        units_in_row = [unit for unit in living_units if unit['location'][1] == y]
        units_in_row = sorted(units_in_row, key=lambda k: k['location'])
        for unit in units_in_row:
            output += (unit['type']+'('+str(unit['hp'])+'),('+str(unit['location'])+')').rjust(20)
        if units_in_row:
            output = output[:-1]
        output += '\n'
    print(output)

def attack_range(unit):
    return [(unit['location'][0], unit['location'][1]+1),
            (unit['location'][0]+1, unit['location'][1]),
            (unit['location'][0]-1, unit['location'][1]),
            (unit['location'][0], unit['location'][1]-1)]

def get_move_grid(cave_map, unit, units):
    max_x = sorted([x[0] for x in cave_map], reverse=True)[0]+1
    max_y = sorted([x[1] for x in cave_map], reverse=True)[0]+1
    living = [unit['location'] for unit in units if unit['hp'] > 0]
    move_grid = {}
    move_grid[unit['location']] = 0
    possible_moves = [unit['location']]
    while len(possible_moves) != 0:
        new_possible = []
        for move in possible_moves:
            move_options = [(move[0], move[1]+1),
                            (move[0]+1, move[1]),
                            (move[0]-1, move[1]),
                            (move[0], move[1]-1)]
            for option in move_options:
                if option not in living and cave_map[option] != '#':
                    distance = move_grid[move] + 1
                    if option not in move_grid or distance < move_grid[option]:
                        move_grid[option] = distance
                        new_possible.append(option)
        possible_moves = new_possible
    return move_grid

def get_next_step(goal, move_grid):
    next_step = goal
    while move_grid[next_step] != 1:
        try:
            if move_grid[(next_step[0], next_step[1]-1)] < move_grid[next_step]:
                next_step = (next_step[0], next_step[1]-1)
                continue
        except KeyError:
            pass
        try:
            if move_grid[(next_step[0]-1, next_step[1])] < move_grid[next_step]:
                next_step = (next_step[0]-1, next_step[1])
                continue
        except KeyError:
            pass
        try:
            if move_grid[(next_step[0]+1, next_step[1])] < move_grid[next_step]:
                next_step = (next_step[0]+1, next_step[1])
                continue
        except KeyError:
            pass
        try:
            if move_grid[(next_step[0], next_step[1]+1)] < move_grid[next_step]:
                next_step = (next_step[0], next_step[1]+1)
                continue
        except KeyError:
            pass
    return next_step

ELF_AP = 10
with open('input.txt') as file:
    data = file.read()
rows = data.splitlines()

cave_map = {}
units = []
max_x = 0
for y in range(len(rows)):
    for x in range(len(rows[y])):
        if x > max_x:
            max_x = x
        if rows[y][x] == 'E':
            cave_map[(x,y)] = '.'
            units.append({'type': 'E', 'location':(x,y), 'hp':200})
        elif rows[y][x] == 'G':
            cave_map[(x,y)] = '.'
            units.append({'type': 'G', 'location':(x,y), 'hp':200})
        else:
            cave_map[(x,y)] = rows[y][x]
max_x += 1


print('Elf Count:',len([unit for unit in units if unit['type'] == 'E' and unit['hp'] > 0]))
print('Initially:')
map_print(cave_map, units)

rounds = 0
combat = True
while combat:
    #print(units)
    for unit in sorted(units, key=lambda k: (k['location'][1], k['location'][0])):
        #print(unit)
        if unit['hp'] <= 0: #skip the dead
            continue
        if unit['type'] == 'E':
            targets = [unit for unit in units if unit['type'] == 'G' and unit['hp'] > 0]
            if len(targets) == 0:
                combat = False
                break
            can_attack = []
            for target in targets:
                if target['location'] in attack_range(unit):
                    can_attack.append(target)
            if len(can_attack) > 0: #attack now
                #print('attacking')
                target = sorted(can_attack, key=lambda k: k['hp'])[0]
                target['hp'] -= ELF_AP
            else: #find a place to move
                #print('moving')
                possible_goals = []
                for target in targets:
                    potential_attack_points = attack_range(target)
                    blocked_points = []
                    for potential_attack_point in potential_attack_points:
                        if cave_map[potential_attack_point] == '#':
                            blocked_points.append(potential_attack_point)
                        elif potential_attack_point in [unit['location'] for unit in units if unit['hp'] > 0]:
                            blocked_points.append(potential_attack_point)
                    possible_goals += list(set(potential_attack_points)-set(blocked_points))

                move_grid = get_move_grid(cave_map, unit, units)
                best_goal = []
                best_distance = None
                for goal in possible_goals:
                    try:
                        _ = move_grid[goal]
                    except KeyError:
                        continue
                    if best_goal == []:
                        best_goal.append(goal)
                        best_distance = move_grid[goal]
                    elif move_grid[goal] < best_distance:
                        best_goal = [goal]
                        best_distance = move_grid[goal]
                    elif move_grid[goal] == best_distance:
                        best_goal.append(goal)
                if best_goal:
                    goal = sorted(best_goal, key=lambda goal: (goal[1], goal[0]))[0]
                    #print('to', goal)
                    next_step = get_next_step(goal, move_grid)
                    #print('via', next_step)
                    unit['location'] = next_step
                    # Try to attack again
                    targets = [unit for unit in units if unit['type'] == 'G' and unit['hp'] > 0]
                    if len(targets) == 0:
                        combat = False
                        break
                    can_attack = []
                    for target in targets:
                        if target['location'] in attack_range(unit):
                            can_attack.append(target)
                    if len(can_attack) > 0: #attack now
                        #print('and attacking')
                        target = sorted(can_attack, key=lambda k: k['hp'])[0]
                        target['hp'] -= ELF_AP

        elif unit['type'] == 'G':
            targets = [unit for unit in units if unit['type'] == 'E' and unit['hp'] > 0]
            if len(targets) == 0:
                combat = False
                break
            can_attack = []
            for target in targets:
                if target['location'] in attack_range(unit):
                    can_attack.append(target)
            if len(can_attack) > 0: #attack now
                #print('attacking')
                target = sorted(can_attack, key=lambda k: k['hp'])[0]
                target['hp'] -= 3
            else: #find a place to move
                #print('moving')
                possible_goals = []
                for target in targets:
                    potential_attack_points = attack_range(target)
                    blocked_points = []
                    for potential_attack_point in potential_attack_points:
                        if cave_map[potential_attack_point] == '#':
                            blocked_points.append(potential_attack_point)
                        elif potential_attack_point in [unit['location'] for unit in units if unit['hp'] > 0]:
                            blocked_points.append(potential_attack_point)
                    possible_goals += list(set(potential_attack_points)-set(blocked_points))

                move_grid = get_move_grid(cave_map, unit, units)
                best_goal = []
                best_distance = None
                for goal in possible_goals:
                    try:
                        _ = move_grid[goal]
                    except KeyError:
                        continue
                    if best_goal == []:
                        best_goal.append(goal)
                        best_distance = move_grid[goal]
                    elif move_grid[goal] < best_distance:
                        best_goal = [goal]
                        best_distance = move_grid[goal]
                    elif move_grid[goal] == best_distance:
                        best_goal.append(goal)
                if best_goal:
                    goal = sorted(best_goal, key=lambda goal: (goal[1], goal[0]))[0]
                    #print('to', goal)
                    next_step = get_next_step(goal, move_grid)
                    #print('via', next_step)
                    unit['location'] = next_step
                    # Try to attack again
                    targets = [unit for unit in units if unit['type'] == 'E' and unit['hp'] > 0]
                    if len(targets) == 0:
                        combat = False
                        break
                    can_attack = []
                    for target in targets:
                        if target['location'] in attack_range(unit):
                            can_attack.append(target)
                    if len(can_attack) > 0: #attack now
                        #print('and attacking')
                        target = sorted(can_attack, key=lambda k: k['hp'])[0]
                        target['hp'] -= 3
    if combat == True:
        rounds += 1
        #print('Rounds:', rounds)
        #map_print(cave_map, units)
    else:
        print('Elf Count:',len([unit for unit in units if unit['type'] == 'E' and unit['hp'] > 0]))
        print('Rounds:', rounds)
        map_print(cave_map, units)
        print('Combat ends after',rounds, 'rounds')
        print('+'.join([str(unit['hp']) for unit in units if unit['hp']>0])+' = '+str(sum([unit['hp'] for unit in units if unit['hp']>0])))
        print(rounds, '*', sum([unit['hp'] for unit in units if unit['hp']>0]), '=', rounds*sum([unit['hp'] for unit in units if unit['hp']>0]))
