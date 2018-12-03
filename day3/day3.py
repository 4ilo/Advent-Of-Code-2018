import re


class Fabric:
    def __init__(self, groups):
        self.id = groups[0]
        self.x = int(groups[1])
        self.y = int(groups[2])
        self.w = int(groups[3])
        self.h = int(groups[4])
        self.intact = True

    def in_range(self, i, j):
        return self.x < i <= self.x + self.w and self.y < j <= self.y + self.h

    def __str__(self):
        return "#{} @ {},{}: {}x{}".format(self.id, self.x, self.y, self.w, self.h)


if __name__ == "__main__":
    # input = open("test.txt").read().splitlines()
    input = open("input.txt").read().splitlines()

    pattern = "#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

    claims = []

    for line in input:
        m = re.match(pattern, line)
        claims.append(Fabric(m.groups()))

    total = 0

    for i in range(1000):
        for j in range(1000):
            count = 0
            for claim in claims:
                if claim.in_range(i, j):
                    count += 1

            if count >= 2:
                total += 1
                for claim in claims:
                    if claim.in_range(i, j) and claim.intact:
                        claim.intact = False

    print("Total: {}".format(total))

    for claim in claims:
        if claim.intact:
            print("Claim {} is intact.".format(claim.id))
            exit(0)
