with open('input.txt') as file:
    data = file.read()
_input = data.split(' ')

players = {}
for x in range(int(_input[0])):
    players[x+1] = 0

last_marble = int(_input[6])*100

current_marble = 0
current_location = 0
marbles = [0]
player = 0

def play_marble(next_marble, current_location):
    global marbles
    global players
    global player
    if next_marble%23 == 0:
        players[player] += next_marble
        remove_loc = (current_location - 7)%len(marbles)
        players[player] += marbles.pop(remove_loc)
        return remove_loc
    else:
        next_location = (current_location + 1)%len(marbles)+1
        marbles.insert(next_location, next_marble)
        return next_location


while current_marble != last_marble:
    player = player%len(players)+1
    current_marble += 1
    current_location = play_marble(current_marble, current_location)

high_score = sorted(players.items(), key=lambda kv: kv[1], reverse=True)[0][1]
print(len(players), 'players; last marble is worth', last_marble, 'points: high score is', high_score)
