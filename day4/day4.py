import re

expr1 = "\[(\d+\-\d+\-\d+) (\d+):(\d+)\] Guard #(\d+)"
expr2 = "\[(\d+\-\d+\-\d+) (\d+):(\d+)\] falls asleep"
expr3 = "\[(\d+\-\d+\-\d+) (\d+):(\d+)\] wakes up"

input = open("test.txt").read().splitlines()
# input = open("input.txt").read().splitlines()
# input.sort()

guards = {}
active = -1

awake_time = -1
sleep_time = 0

for line in input:
    print(line)

    # Start shift
    m = re.match(expr1, line)
    if m:
        date, hour, time, id = m.groups()

        if awake_time != -1:
            test = list(guards[active].keys())[-1]
            guard = guards[active][test]
            for x in range(awake_time, int(60)):
                guard[x] = True

            awake_time = -1

        active = int(id)

        awake_time = int(time)
        if int(hour) != 0:
            awake_time = 0
            date_list = list(date)
            date_list[-1] = str(int(date[-1])+1)
            date = ''.join(date_list)

        if active not in guards:
            guards.update({
                active: {
                    date: [False for i in range(60)]
                }
            })
        else:
            guard = guards[active]
            guard.update({
                date: [False for i in range(60)]
            })

    # Goto sleep
    m = re.match(expr2, line)
    if m:
        date, hour, sleep = m.groups()

        guard = guards[active][date]
        for x in range(awake_time, int(sleep)):
            guard[x] = True

        awake_time = -1

    # Wake up
    m = re.match(expr3, line)
    if m:
        date, hour, up = m.groups()

        awake_time = int(up)

pass