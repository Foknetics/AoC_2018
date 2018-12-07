def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2-x1)+abs(y2-y1)

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

infinite_ids = []
for x in range(min_x, min_x+max_x):
    for y in range(min_y, min_y+max_y):
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
