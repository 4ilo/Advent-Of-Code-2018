import re

result = []


def step(letters1, letters2):
    for letter in letters1:
        if letter not in letters2:
            result.append(letter)
            remove = [i for i, x in enumerate(letters1) if x == letter]

            letters1_new = []
            letters2_new = []

            for i in range(len(letters1)):
                if i not in remove:
                    letters1_new.append(letters1[i])
                    letters2_new.append(letters2[i])

            if len(letters1_new) > 1:
                step(letters1_new, letters2_new)
            else:
                result.append(letters1_new[0])
                result.append(letters2_new[0])
            break


if __name__ == "__main__":
    input = open('test.txt').read().splitlines()
    # input = open('input.txt').read().splitlines()

    data = []
    for line in input:
        m = re.match("Step (\w) must be finished before step (\w) can begin", line)
        if m:
            data.append(m.groups())

    data.sort(key=lambda tup: tup[0])

    letters1 = []
    letters2 = []
    for line in data:
        letters1.append(line[0])
        letters2.append(line[1])

    step(letters1, letters2)

    print('Result: {}'.format(''.join(result)))
