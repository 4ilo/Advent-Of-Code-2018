
def react(input):
    data = list(input)

    removed = False

    while not removed:
        removed = True
        for i in range(len(data)):
            if i + 1 < len(data):
                if abs(ord(data[i]) - ord(data[i + 1])) == 32:
                    removed = False
                    data.pop(i)
                    data.pop(i)
    return data


if __name__ == "__main__":
    #input = "dabAcCaCBAcCcaDA"
    input = open("input.txt").read()

    data = list(input)

    # Part 1
    data = react(data)
    print("Part 1: {}".format(len(data)))

    # Part 2
    best = 1000000
    occurance = [x for x in set(data)]
    for letter in occurance:
        data2 = list(filter(lambda a: a != letter.lower(), data))
        data2 = list(filter(lambda a: a != letter.upper(), data2))
        data2 = react(data2)

        if len(data2) < best:
            best = len(data2)

    print("Part 2: {}".format(best))

