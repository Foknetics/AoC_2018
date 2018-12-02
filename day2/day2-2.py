from collections import Counter


with open('input.txt') as file:
    data = file.read()

def similar_id(id_1, id_2):
    one_miss = False
    for index, letter in enumerate(id_1):
        if one_miss and letter != id_2[index]:
            return False
        elif letter != id_2[index]:
            one_miss = True
    return True

boxes = data.splitlines()

for box in boxes:
    for other_box in boxes:
        if other_box == box:
            continue
        elif similar_id(box, other_box):
            print(box, other_box)
