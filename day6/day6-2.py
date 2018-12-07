max_distance = 10000
with open('input.txt') as file:
    data = file.read()

def manhattan_distance(point1, point2):
    x_distance = point2[0] - point1[0]
    y_distance = point2[1] - point1[1]
    return abs(x_distance)+abs(y_distance)

def total_distance(point, dataset):
    total = 0
    for _id in dataset:
        total += manhattan_distance(point, dataset[_id])
    return total

points = [(int(coordinate[1]), int(coordinate[0])) for coordinate in [coordinate.split(', ') for coordinate in data.splitlines()]]
ids = [chr(x+65) for x in range(len(data.splitlines()))]

dataset = {}
for x in range(len(ids)):
    dataset[ids[x]] = points[x]

min_x = points[0][0]
min_y = points[0][1]
max_x = min_x
max_y = min_y
data_map = {}
for _id, point in dataset.items():
    if point[0] > max_x:
        max_x = point[0]
    elif point[0] < min_x:
        min_x = point[0]
    if point[1] > max_y:
        max_y = point[1]
    elif point[1] < min_y:
        min_y = point[1]
    data_map[(point[0], point[1])] = _id

count = 0
for x in range(min_x, min_x+max_x):
    for y in range(min_y, min_y+max_y):
        if total_distance((x,y), dataset) < max_distance:
            count += 1
            if (x, y) not in data_map:
                data_map[(x, y)] = '#'
        elif (x, y) not in data_map:
                data_map[(x, y)] = '.'

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