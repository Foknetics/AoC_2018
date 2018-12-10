with open('input.txt') as file:
    data = file.read()

units = [chr(x+97) for x in range(26)]
one_side = [unit+unit.upper() for unit in units]
other_side = [reaction[::-1] for reaction in one_side]
reaction_set = one_side + other_side

def remove_reaction(polymer):
    reacting = True
    while reacting:
        reacting = False
        for reaction in reaction_set:
            try:
                polymer.index(reaction)
                polymer = polymer.replace(reaction, '')
                reacting = True
            except ValueError:
                continue
        if not reacting:
            return polymer

final_polymer = remove_reaction(data)
print('The resulting polymer contains', len(final_polymer), 'units.')
