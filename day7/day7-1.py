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

solution = ''
while len(solution) != len(steps):
    dependencies = [x[1] for x in step_dependencies]
    possible_steps = [step for step in steps_left if step not in dependencies]
    next_step = sorted(possible_steps)[0]
    solution += next_step
    steps_left.remove(next_step)
    steps_to_remove = []
    for step_dependency in step_dependencies:
        if step_dependency[0] == next_step:
            steps_to_remove.append(step_dependency)
    for step_to_remove in steps_to_remove:
        del step_dependencies[step_dependencies.index(step_to_remove)]

print('The sleigh should be built in the following order:', solution)