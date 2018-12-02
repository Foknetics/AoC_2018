from collections import Counter


with open('input.txt') as file:
    data = file.read()

appears_twice = 0
appears_thrice = 0

for box_id in data.splitlines():
    letter_counts = Counter(box_id)
    twice_match = False
    thrice_match = False
    for letter in letter_counts:
        if letter_counts[letter] == 2:
            twice_match = True
        if letter_counts[letter] == 3:
            thrice_match = True
        if twice_match and thrice_match:
            break
    if twice_match:
        appears_twice += 1
    if thrice_match:
        appears_thrice += 1

print(appears_twice, '*', appears_thrice, '=', appears_twice*appears_thrice)
