
# input = open("test.txt").read().splitlines()
# input = open("test2.txt").read().splitlines()
input = open("input.txt").read().splitlines()

# Part 1
twos = 0
threes = 0
for line in input:
    letters = list(line)

    two = False
    three = False
    for letter in set(letters):
        if letters.count(letter) == 2:
            two = True

        if letters.count(letter) == 3:
            three = True

    if two:
        twos += 1
    if three:
        threes += 1

print("Checksum: {}".format(twos * threes))

# Part 2
data = [list(line) for line in input]
for line in data:
    for line2 in data:
        dif = []
        for i in range(len(line)-1):
            if line[i] != line2[i]:
                dif.append(i)

        if len(dif) == 1:
            del line[dif[0]]
            print("Matched string: {}".format("".join(line)))
            exit(0)
