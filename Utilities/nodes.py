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


class AVLTreeNode:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1


class HeapNode:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


class PQNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
