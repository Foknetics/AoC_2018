skip = 77201
skip += 10

recipes = [3, 7]
elf1 = 0
elf2 = 1

#print(recipes)
while len(recipes) < skip:
    sum_of_recipes = recipes[elf1]+recipes[elf2]
    for x in range(len(str(sum_of_recipes))):
        recipes.append(int(str(sum_of_recipes)[x]))
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    #print(recipes)
if len(recipes) > skip:
    recipes = recipes[:skip]
print('The 10 recipes after',skip-10,'are', ''.join([str(x) for x in recipes[-10:]]))