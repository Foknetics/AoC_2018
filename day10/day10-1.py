with open('input.txt') as file:
    data = file.read()

def board_print(positons):
    points = [positions[x]['coord'] for x in positions]
    board = ''
    x_offset = 150
    y_offset = 100
    for x in range(x_offset, 70+x_offset):
        for y in range(y_offset, 236+y_offset):
            if (x, y) in points:
                board += '#'
            else:
                board += '.'
        board += '\n'
    print(board[:-1])

positions = {}
file_data = data.splitlines()
for coord in range(len(file_data)):
    x, y = file_data[coord][file_data[coord].index('<')+1: file_data[coord].index('>')].split(', ')
    x_vel, y_vel = file_data[coord][file_data[coord].index('y=')+3: -1].split(', ')
    positions[coord] = {'coord': (int(y), int(x)), 'x_vel': int(y_vel), 'y_vel': int(x_vel)}

frame = 0
while True:
    frame += 1
    for _id, pos in positions.items():
        pos['coord'] = (pos['coord'][0]+pos['x_vel'], pos['coord'][1]+pos['y_vel'])
    if frame == 10086:
        print(frame)
        board_print(positions)
        break
