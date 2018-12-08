
class Node:
    def __init__(self, data):
        """ Construct the tree """
        self.child_nodes = []
        self.metadata = []

        childs = data.pop(0)
        meta = data.pop(0)

        for i in range(childs):
            self.child_nodes.append(Node(data))

        for i in range(meta):
            self.metadata.append(data.pop(0))

    def count_meta(self):
        """ Sum of metadata entrys for part 1 """
        total = sum(self.metadata)
        for node in self.child_nodes:
            total += node.count_meta()

        return total

    def value(self):
        """ Calculate the 'value' of each node for part 2 """
        value = 0
        if len(self.child_nodes) == 0:
            return sum(self.metadata)

        for i in self.metadata:
            if i-1 < len(self.child_nodes):
                value += self.child_nodes[i-1].value()

        return value


if __name__ == "__main__":
    # input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    input = open("input.txt").read()
    data = [int(x) for x in input.split(' ')]

    root = Node(data)

    print("Part1: {}".format(root.count_meta()))
    print("Part2: {}".format(root.value()))
