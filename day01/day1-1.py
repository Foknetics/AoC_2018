with open('input.txt') as file:
    data = file.read()

frequency = 0
for frequency_change in data.splitlines():
    frequency += int(frequency_change)
print('Ending frequency:', frequency)
