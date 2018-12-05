with open('test.txt') as file:
    data = file.read()

frequency_changes = data.splitlines()

frequency = 0
possible_matches = []
for frequency_change in frequency_changes:
    frequency += int(frequency_change)
    possible_matches.append(frequency)

match_found = False
while not match_found:
    for frequency_change in frequency_changes:
        frequency += int(frequency_change)
        if frequency in possible_matches:
            print('First frequency repeat:', frequency)
            match_found = True
            break
