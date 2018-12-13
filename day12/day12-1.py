with open('input.txt') as file:
    data = file.read().splitlines()

gen_map = {}
index = 0
for plant in data[0].split()[2]:
    gen_map[index] = plant
    index += 1

data_rules = data[2:]
rules = []
outcomes = []
for rule in data_rules:
    parts = rule.split()
    rules.append(parts[0])
    outcomes.append(parts[2])

#print(' 0:',''.join([gen_map[x] for x in sorted(gen_map)]))
for generation in range(1, 21):
    new_min = min(gen_map.keys()) - 2
    new_max = max(gen_map.keys()) + 4
    new_gen_map = gen_map.copy()
    for plant in range(new_min, new_max):
        state = gen_map.get(plant-2, '.')
        state += gen_map.get(plant-1, '.')
        state += gen_map.get(plant, '.')
        state += gen_map.get(plant+1, '.')
        state += gen_map.get(plant+2, '.')
        #print(plant, state)
        try:
            new_gen_map[plant] = outcomes[rules.index(state)]
        except ValueError:
            new_gen_map[plant] = '.'
    gen_map = new_gen_map.copy()
    #print(str(generation).rjust(2)+':',''.join([gen_map[x] for x in sorted(gen_map)]))

total = 0
for index, value in gen_map.items():
    if value == '#':
        total += index
print('Sum of id of plant containing pots is', total)
