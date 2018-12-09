from collections import deque


def play_marbles(players, last):
    scores = [0 for x in range(players)]

    current_player = 0
    current_marble = 0

    circle = deque()
    circle.append(0)

    for marble in range(1, last+1):
        if marble % 23 == 0:
            scores[current_player] += marble
            index = (current_marble - 7) % len(circle)
            scores[current_player] += circle[index]
            del circle[index]
            current_marble = index
        else:
            index = (current_marble+1) % len(circle) + 1
            circle.insert(index, marble)
            current_marble = index

        current_player += 1
        if current_player >= players:
            current_player = 0

    return max(scores)


if __name__ == '__main__':
    print("Part 1: {}".format(play_marbles(493, 71863)))
    print("Part 2: {}".format(play_marbles(493, 71863 * 100)))
