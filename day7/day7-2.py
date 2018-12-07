delay = 60
elves = []
for x in range(1, 5):
    elves.append({'current': None, 'left': 0})

with open('input.txt') as file:
    data = file.read()

steps = []
step_dependencies = []
for line in data.splitlines():
    splits = line.split()
    step_dependencies.append((splits[1], splits[7]))
    if splits[1] not in steps:
        steps.append(splits[1])
    if splits[7] not in steps:
        steps.append(splits[7])
steps_left = steps.copy()

in_prog = []
solution = ''
total_time = -1

def available_jobs(step_dependencies, in_prog):
    dependencies = [x[1] for x in step_dependencies]
    step_dependencies = [step for step in steps_left if step not in dependencies]
    return sorted(list(set(step_dependencies).difference(set(in_prog))))

while len(solution) != len(steps):
    total_time += 1
    for elf in elves:
        if elf['current'] != None:
            elf['left'] += -1
    for elf in elves:
        if elf['current'] != None and elf['left'] == 0:
            solution += elf['current']
            steps_left.remove(elf['current'])
            steps_to_remove = []
            for step_dependency in step_dependencies:
                if step_dependency[0] == elf['current']:
                    steps_to_remove.append(step_dependency)
            for step_to_remove in steps_to_remove:
                del step_dependencies[step_dependencies.index(step_to_remove)]
            in_prog.remove(elf['current'])
            elf['current'] = None
    possible_steps = available_jobs(step_dependencies, in_prog)
    for elf in elves:
        if elf['current'] == None:
            if len(possible_steps) != 0:
                elf['current'] = possible_steps[0]
                possible_steps.remove(elf['current'])
                in_prog.append(elf['current'])
                elf['left'] = ord(elf['current'])-64+delay

print('The sleigh should be built in the following order:', solution)
print('It will take', total_time, 'seconds to build with', len(elves), 'elves.')