class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class HeapNode:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
