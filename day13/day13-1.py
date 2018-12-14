#def train_print(track_map, trains):
#    max_x = sorted([x[0] for x in track_map], reverse=True)[0]+1
#    max_y = sorted([x[1] for x in track_map], reverse=True)[0]+1
#    locations = [x['location'] for x in trains]
#    output = ' '+''.join([str(x)[-1] for x in range(max_x)])+'\n'
#    for y in range(max_y):
#        output += str(y)
#        for x in range(max_x):
#            if (x,y) in locations:
#                output += trains[locations.index((x,y))]['state']
#            else:
#                output += track_map.get((x,y), ' ')
#        output += '\n'
#    print(output)

with open('test.txt') as file:
    data = file.read()
rows = data.splitlines()

track_map = {}
trains = []
max_x = 0
for y in range(len(rows)):
    for x in range(len(rows[y])):
        if x > max_x:
            max_x = x
        if rows[y][x] not in ['|','/','-','\\','+', ' ']:
            if rows[y][x] in ['<', '>']:
                track_map[(x,y)] = '-'
            else:
                track_map[(x,y)] = '|'
            trains.append({'location':(x,y), 'state': rows[y][x], 'turns': 0})
        else:
            track_map[(x,y)] = rows[y][x]
max_x += 1

#print('Original Track')
#output = ' '+''.join([str(x)[-1] for x in range(max_x)])+'\n'
#for y in range(len(rows)):
#    output += str(y)
#    for x in range(max_x):
#        output += track_map.get((x,y), ' ')
#    output += '\n'
#print(output[:-1])

crash = False
#tick = 0
#print('\nTick 0:')
#train_print(track_map, trains)
while not crash:
    #tick += 1
    for train in sorted(trains, key=lambda k: k['location']):
        if train['state'] == '^':
            new_location = (train['location'][0], train['location'][1]-1)
            movement = 'up'
        elif train['state'] == '>':
            new_location = (train['location'][0]+1, train['location'][1])
            movement = 'right'
        elif train['state'] == 'v':
            new_location = (train['location'][0], train['location'][1]+1)
            movement = 'down'
        elif train['state'] == '<':
            new_location = (train['location'][0]-1, train['location'][1])
            movement = 'left'

        new_track = track_map[new_location]
        if new_location in [x['location'] for x in trains]:
            print('Train collision at', new_location)
            train['location'] = new_location
            train['state'] = 'X'
            crash = True
            break
        elif new_track == '|':
            new_state = train['state']
        elif new_track == '/':
            if movement is 'left':
                new_state = 'v'
            elif movement is 'right':
                new_state = '^'
            elif movement is 'down':
                new_state = '<'
            elif movement is 'up':
                new_state = '>'
        elif new_track == '-':
            new_state = train['state']
        elif new_track == '\\':
            if movement is 'right':
                new_state = 'v'
            elif movement is 'left':
                new_state = '^'
            elif movement is 'down':
                new_state = '>'
            elif movement is 'up':
                new_state = '<'
        elif new_track == '+':
            turns = train['turns']%3
            train['turns'] += 1
            states = ['^', '>', 'v', '<']
            if turns == 0:
                new_state = states[(states.index(train['state'])-1)%4]
            elif turns == 1:
                new_state = train['state']
            elif turns == 2:
                new_state = states[(states.index(train['state'])+1)%4]

        train['location'] = new_location
        train['state'] = new_state
    #print('\nTick'+str(tick)+':')
    #train_print(track_map, trains)
