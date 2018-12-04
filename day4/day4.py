import re
import datetime

expr1 = "\[(\d+\-\d+\-\d+) (\d+):(\d+)\] Guard #(\d+)"
expr2 = "\[(\d+\-\d+\-\d+) (\d+):(\d+)\] falls asleep"
expr3 = "\[(\d+\-\d+\-\d+) (\d+):(\d+)\] wakes up"
date_rx = "\[(\d+)-(\d+)-(\d+)\ (\d+):(\d+)]"


def sort_input(input):
    lines = []

    for line in input:
        m = re.match(date_rx, line)
        y, m, d, hh, mm = m.groups()
        date = datetime.datetime(year=int(y), month=int(m), day=int(d), hour=int(hh), minute=int(mm))
        lines.append((date, line))

    lines.sort(key=lambda i: i[0])
    return lines


if __name__ == "__main__":
    # input = open("test.txt").read().splitlines()
    input = open("input.txt").read().splitlines()

    input = sort_input(input)
    input = [x[1] for x in input]

    guards = {}
    active = -1

    sleep_time = -1

    # Convert input to data structure
    for line in input:
        # Start shift
        m = re.match(expr1, line)
        if m:
            date, hour, time, id = m.groups()

            if sleep_time != -1:
                test = list(guards[active].keys())[-1]
                guard = guards[active][test]
                for x in range(sleep_time, int(60)):
                    guard[x] = False

                sleep_time = -1

            active = int(id)

            if int(hour) != 0:
                date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                date_obj = date_obj + datetime.timedelta(days=1)
                date = date_obj.strftime('%Y-%m-%d')

            if active not in guards:
                guards.update({
                    active: {
                        date: [True for i in range(60)]
                    }
                })
            else:
                guard = guards[active]
                guard.update({
                    date: [True for i in range(60)]
                })

        # Goto sleep
        m = re.match(expr2, line)
        if m:
            date, hour, sleep = m.groups()
            sleep_time = int(sleep)

        # Wake up
        m = re.match(expr3, line)
        if m:
            date, hour, up = m.groups()

            guard = guards[active][date]
            for x in range(sleep_time, int(up)):
                guard[x] = False

            sleep_time = -1

    # Calcualte part 1
    minutes = [[0 for x in range(60)] for y in range(len(guards))]
    total_sleep = [0 for y in range(len(guards))]
    for i in range(60):
        for x, (id, guard) in enumerate(guards.items()):
            for day, hours in guard.items():
                if not hours[i]:
                    total_sleep[x] += 1
                    minutes[x][i] += 1

    test = total_sleep.index(max(total_sleep))
    guard = list(guards.keys())[test]

    min_max = minutes[test].index(max(minutes[test]))

    print("Guard: {}, minute: {}, result: {}".format(guard, min_max, guard*min_max))

    # Part2
    combined = [j for i in minutes for j in i]
    max = max(combined)
    for i, minute in enumerate(minutes):
        if max in minute:
            min_max = minute.index(max)
            guard = list(guards.keys())[i]
            print("PART2: Guard: {}, minute: {}, result: {}".format(guard, min_max, guard*min_max))
            exit(0)

