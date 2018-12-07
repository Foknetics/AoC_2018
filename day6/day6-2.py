max_distance = 10000

with open('input.txt') as file:
    data = file.read().splitlines()

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2-x1)+abs(y2-y1)

def inside_max(point, dataset):
    total = 0
    for _id in dataset:
        total += manhattan_distance(point, dataset[_id])
        if total >= max_distance:
            return False
    return True

points = [(int(coordinate[1]), int(coordinate[0])) for coordinate in [coordinate.split(', ') for coordinate in data]]
ids = [chr(x+65) for x in range(len(data))]

dataset = {}
for _id, point in zip(ids, points):
    dataset[_id] = point

min_x, min_y = points[0]
max_x, max_y = points[0]

data_map = {}
for _id, point in dataset.items():
    x, y = point
    if x > max_x:
        max_x = x
    elif x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    elif y < min_y:
        min_y = y
    data_map[(x, y)] = _id

count = 0
for x in range(min_x, min_x+max_x):
    for y in range(min_y, min_y+max_y):
        if inside_max((x,y), dataset):
            count += 1
        #    if (x, y) not in data_map:
        #        data_map[(x, y)] = '#'
        #elif (x, y) not in data_map:
        #        data_map[(x, y)] = '.'

#display_map = '  '+''.join([str(y) for y in range(min_y, min_y+max_y)])+'\n'
#for x in range(min_x, min_x+max_x):
#    display_map += str(x)+' '
#    for y in range(min_y, min_y+max_y):
#        display_map += data_map[(x, y)]
#    display_map += '\n'
#display_map = display_map[:-1]
#print(display_map)
#print()
print('The size of the region containing all locations which have a total distance to all given coordinates of less than',max_distance, 'is', count)