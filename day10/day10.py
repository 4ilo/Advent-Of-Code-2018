import re
import copy


class Point:
    def __init__(self, values):
        self.x = int(values[0])
        self.y = int(values[1])
        self.speed_x = int(values[2])
        self.speed_y = int(values[3])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y


def print_field(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            print(field[y][x], end="")
        print("")


def draw_points(points, w, h, big_min):
    field = [['.' for x in range(w)] for y in range(h)]
    for point in points:
        field[point.y + abs(big_min[1])][point.x + abs(big_min[0])] = '#'

    print_field(field)

    return field


def find_range(points):
    big_pos = [0, 0]
    big_neg = [0, 0]

    for point in points:
        if point.x > big_pos[0]:
            big_pos[0] = point.x

        if point.x < big_neg[0]:
            big_neg[0] = point.x

        if point.y > big_pos[1]:
            big_pos[1] = point.y

        if point.y < big_neg[1]:
            big_neg[1] = point.y

    width = big_pos[0] + abs(big_neg[0]) + 1
    heigth = big_pos[1] + abs(big_neg[1]) + 1

    return width, heigth, big_neg


if __name__ == "__main__":
    expr = "position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>"

    #input = open("test.txt").read().splitlines()
    input = open("input.txt").read().splitlines()

    # Parse points
    points = []
    for line in input:
        m = re.match(expr, line)
        if m:
            points.append(Point(m.groups()))

    smallest = {
        'i': 0,
        'points': [],
        'width': 10000,
        'height': 10000,
    }

    for x in range(15000):
        width, heigth, _ = find_range(points)

        # This iteration gives the smallest result
        if width < smallest['width'] or heigth < smallest['height']:
            smallest.update({
                'width': width,
                'height': heigth,
                'i': x,
                'points': copy.deepcopy(points)
            })

        # Move all points
        for point in points:
            point.move()

    print("smallest field")
    print("After {} seconds".format(smallest['i']))

    width, heigth, neg = find_range(smallest['points'])
    draw_points(smallest['points'], width, heigth, neg)
