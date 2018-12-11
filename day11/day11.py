from multiprocessing import Pool

def power_level(point, serial_number):
    rack_id = point[0] + 10
    power_lvl = rack_id * point[1]
    power_lvl += serial_number
    power_lvl *= rack_id
    power_lvl = power_lvl // 10**2 % 10
    power_lvl -= 5
    return power_lvl


def part1(args):
    kernel_size, grid = args
    best = []
    best_sum = 0

    for y in range(size - kernel_size):
        for x in range(size - kernel_size):
            sum = 0
            for i in range(kernel_size):
                for j in range(kernel_size):
                    val = grid[y + i][x + j]
                    sum += grid[y + i][x + j]

            if sum > best_sum:
                best_sum = sum
                best = [x, y]

    return best, best_sum


if __name__ == "__main__":
    size = 300
    serial_number = 3463

    grid = [[0 for x in range(size)] for y in range(size)]

    for y in range(size):
        for x in range(size):
            grid[y][x] = power_level((x,y), serial_number)

    result = part1((3, grid))
    print("Part1: {},{}".format(result[0][0], result[0][1]))

    # Part 2
    p = Pool(8)
    results = p.map(part1, [(x, grid) for x in range(size)])

    best = 0
    best_size = 0
    best_sum = 0
    for x, result in enumerate(results):
        if result[1] > best_sum:
            best_sum = result[1]
            best_size = x
            best = result[0]

    print("Part2: {},{},{}".format(best[0], best[1], best_size))
