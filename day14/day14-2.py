goal = '077201'

recipes = [3, 7]
elf1 = 0
elf2 = 1

match = False
while not match:
    sum_of_recipes = recipes[elf1]+recipes[elf2]
    for x in range(len(str(sum_of_recipes))):
        recipes.append(int(str(sum_of_recipes)[x]))
        if ''.join([str(x) for x in recipes[len(goal)*-1:]]) == goal:
            match = True
            break
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print(goal, 'first appears after', len(recipes)-len(goal), 'recipes')