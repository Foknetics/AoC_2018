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

#print('Date   ID     Minute')
#print('              000000000011111111112222222222333333333344444444445555555555')
#print('              012345678901234567890123456789012345678901234567890123456789')
#for day in days:
#    print(day, ' '+days[day]['guard'].ljust(5, ' ')+' ',''.join(days[day]['sleep']))

guard_sleeps = {}
for day in days:
    guard = days[day]['guard']
    try:
        guard_sleeps[guard] += days[day]['sleep'].count('#')
    except KeyError:
        guard_sleeps[guard] = days[day]['sleep'].count('#')

sleepy_guard = sorted(guard_sleeps.items(), key=lambda kv: kv[1], reverse=True)[0][0]

minute_likelihood = {}
for day in days:
    if days[day]['guard'] != sleepy_guard:
        continue
    for x in range(60):
        if days[day]['sleep'][x] == '#':
            try:
                minute_likelihood[x] += 1
            except KeyError:
                minute_likelihood[x] = 1

best_minute = sorted(minute_likelihood.items(), key=lambda kv: kv[1], reverse=True)[0][0]

print(int(sleepy_guard[1:]), '*', best_minute, '=', int(sleepy_guard[1:])*best_minute)
