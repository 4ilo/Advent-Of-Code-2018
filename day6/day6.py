
def printfield(field):
    for x in field:
        for y in x:
            print(y, end=" ")
        print("")

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

input = open("test.txt").read().splitlines()
#input = open("input.txt").read().splitlines()
size = 1000

data = []
for point in input:
    temp = point.split(", ")
    data.append((int(temp[0]), int(temp[1])))

print(data)

field = [[-1 for x in range(size)] for y in range(size)]

for x in range(size):
    for y in range(size):

        min_dist = 100000
        second_dist = 1000000
        closest = -1
        second = -1

        for point in data:
            dist = distance((x, y), point)
            if dist < min_dist:
                second_dist = min_dist
                second = closest

                min_dist = dist
                closest = data.index(point)

            elif dist == min_dist:
                closest = -1

            elif dist < second_dist:
                second_dist = dist
                second = data.index(point)

        field[y][x] = closest

#printfield(field)

exclude = set()
for x in range(size):
    for y in range(size):
        if (x == 0 or x == size -1) and (y == 0 or y == size-1):
            exclude.add(field[y][x])

print(exclude)
loop = [x for x in range(len(data)) if x not in exclude]
print(loop)

biggest = 0
for number in loop:
    sum = 0
    for row in field:
        sum += row.count(number)

    if sum > biggest:
        biggest = sum

print(biggest)

