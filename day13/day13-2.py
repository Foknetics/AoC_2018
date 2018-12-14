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

while True:
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
            other_train = [train for train in trains if train['location'] == new_location][0]
            trains.remove(train)
            trains.remove(other_train)
            continue
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
    if len(trains) == 1:
        print('Last train ends at',trains[0]['location'])
        break
