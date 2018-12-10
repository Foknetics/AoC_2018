def timestamp(data_line):
    return data_line[1:17]

with open('input.txt') as file:
    data = file.read()

split_data = data.splitlines()
sorted_data = sorted(split_data, key=timestamp)

days = {}
fell_asleep = None
for line in sorted_data:
    split_line = line.split()
    date = split_line[0][6:]
    time = split_line[1][:-1]
    action = split_line[2]
    if action == 'Guard':
        if fell_asleep != None:
            for x in range(60-int(fell_asleep)):
                days[key]['sleep'][x+int(fell_asleep)] = '#'
        guard = split_line[3]
        if time[:2] == '23':
            key = date[:2]+'-'+str(int(date[3:])+1).rjust(2, '0')
        else:
            key = date
        days[key] = {'guard': guard, 'sleep': ['.' for x in range(60)]}
        fell_asleep = None
    elif action == 'falls':
        fell_asleep = time[3:]
    else:
        for x in range(int(time[3:])-int(fell_asleep)):
            days[key]['sleep'][x+int(fell_asleep)] = '#'
        fell_asleep = None

guard_sleeps = {}
for day in days:
    guard = days[day]['guard']
    if guard not in guard_sleeps:
        guard_sleeps[guard] = [0 for x in range(60)]
    for x in range(60):
        if days[day]['sleep'][x] == '#':
            guard_sleeps[guard][x] += 1

guard_frequency = {}
for guard in guard_sleeps:
    prime_data = sorted({x: guard_sleeps[guard][x] for x in range(60)}.items(), key=lambda kv: kv[1], reverse=True)[0]
    guard_frequency[guard] = prime_data

frequent_guard = sorted(guard_frequency.items(), key=lambda kv: kv[1][1], reverse=True)[0]

print(int(frequent_guard[0][1:]), '*', int(frequent_guard[1][0]), '=', int(frequent_guard[0][1:])*int(frequent_guard[1][0]))
