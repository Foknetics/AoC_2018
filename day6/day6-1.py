def manhattan_distance(point1, point2):
    x_distance = point2[0] - point1[0]
    y_distance = point2[1] - point1[1]
    return abs(x_distance)+abs(y_distance)

def least_or_blank(distances):
    sorted_distances = sorted(distances.items(), key=lambda kv: kv[1])
    a = sorted_distances[0][1]
    if sorted_distances[1][1] == a:
        return '.'
    return sorted_distances[0][0]

with open('input.txt') as file:
    data = file.read()

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

infinite_ids = []
for x in range(min_x-10, min_x+max_x):
    for y in range(min_y-10, min_y+max_y):
        distances = {}
        for _id, point in dataset.items():
            distances[_id] = manhattan_distance((x,y), point)
        data_map[(x, y)] = least_or_blank(distances)
        if data_map[(x, y)] not in infinite_ids:
            if x==min_x or x==max_x or y==min_y or y==max_y:
                infinite_ids.append(data_map[(x, y)])

#display_map = ' '+''.join([str(y) for y in range(min_y, min_y+max_y)])+'\n'
#for x in range(min_x, min_x+max_x):
#    display_map += str(x)
#    for y in range(min_y, min_y+max_y):
#        display_map += data_map[(x, y)]
#    display_map += '\n'
#display_map = display_map[:-1]
#print(display_map)

largest_area = 0
for _id in dataset.keys():
    if _id in infinite_ids:
        continue
    if dataset[_id][0] not in [min_x, max_x] and dataset[_id][1] not in [min_y, max_y]:
        area_of_id = len([x for x in data_map if data_map[x] == _id])
        if area_of_id > largest_area:
            largest_area = area_of_id

print('The size of the largest area that is not infite is', largest_area)
