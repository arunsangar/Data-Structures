class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            for x in line.split():
                data.append(int(x))
    return data
