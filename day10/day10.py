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


expr = "position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>"

#input = open("test.txt").read().splitlines()
input = open("input.txt").read().splitlines()

width = 25
heigth = 16

points = []
for line in input:
    m = re.match(expr, line)
    if m:
        points.append(Point(m.groups()))

smallest = [10000, 10000]
smallest_points = []
smallest_i = 0

for x in range(15000):
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

    #print("Second {}".format(x))
    width = big_pos[0] + abs(big_neg[0]) + 1
    heigth = big_pos[1] + abs(big_neg[1]) + 1

    if width < smallest[0] or heigth < smallest[1]:
        smallest = [width, heigth]
        smallest_i = x
        smallest_points = copy.deepcopy(points)
        #field = draw_points(points, width, heigth, big_neg)
        #smallest_field = field

    for point in points:
        point.move()


print("smallest field")
print(smallest)
print(smallest_i)

big_pos = [0, 0]
big_neg = [0, 0]
for point in smallest_points:
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
draw_points(smallest_points, width, heigth, big_neg)
#print_field(smallest_field)
