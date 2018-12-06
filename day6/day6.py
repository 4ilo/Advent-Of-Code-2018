
def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


if __name__ == "__main__":
    # input = open("test.txt").read().splitlines()
    input = open("input.txt").read().splitlines()
    size = 400
    treshold = 10000

    data = []
    for point in input:
        temp = point.split(", ")
        data.append((int(temp[0]), int(temp[1])))

    field = [[-1 for x in range(size)] for y in range(size)]
    exclude = set()

    for x in range(size):
        for y in range(size):
            dists = []

            for nr, point in enumerate(data):
                dist = distance((x, y), point)
                dists.append((nr, dist))

            dists.sort(key=lambda a: a[1])
            if dists[0][1] != dists[1][1]:
                field[y][x] = dists[0][0]

            if (x == 0 or x == size -1) or (y == 0 or y == size-1):
                exclude.add(field[y][x])

    biggest = 0
    for number in [x for x in range(len(data)) if x not in exclude]:
        sum = 0
        for row in field:
            sum += row.count(number)

        if sum > biggest:
            biggest = sum

    print("Part1: {}".format(biggest))

    # Part 2
    area = 0
    for x in range(size):
        for y in range(size):
            dist_sum = 0

            for point in data:
                dist = distance((x, y), point)
                dist_sum += dist

            if dist_sum < treshold:
                area += 1

    print("Part2: {}".format(area))
