from Utilities.nodes import TreeNode
from Utilities.make_list import inorder
from Utilities.make_list import preorder
from Utilities.make_list import postorder
from Utilities.helper import print_list


class BSTRecursive:

    def __init__(self):
        self.__root = None

    # insert specified node in the BST
    # does not insert if duplicate node
    def insert(self, data, current=None):
        if(self.empty()):
            self.__root = TreeNode(data)
        elif(current is None):
            self.insert(data, self.__root)
        # left subtree
        elif(current.data > data):
            # if empty, add node
            if(current.left is None):
                current.left = TreeNode(data)
            # else recurse down left subtree
            else:
                self.insert(data, current.left)
        # right subtree
        elif(current.data < data):
            # if empty, add node
            if(current.right is None):
                current.right = TreeNode(data)
            # else recurse down right subtree
            else:
                self.insert(data, current.right)
        # duplicate node condition
        else:
            return

    # delete specified node from the BST
    def delete(self, data, current=None, previous=None):
        if(self.empty()):
            return
        elif(current is None and previous is None):
            self.delete(data, self.__root, None)
        # traverse down left subtree
        elif(current.data > data):
            self.delete(data, current.left, current)
        # traverse down right subtree
        elif(current.data < data):
            self.delete(data, current.right, current)
        # current nodes is set for deletion
        else:
            # node has at most one child
            if(current.left is None or current.right is None):
                child = None
                # choose child to replace current node
                if(current.left is None):
                    child = current.right
                else:
                    child = current.left
                # node is root
                if(previous is None):
                    self.__root = child
                    current = None
                    return
                # replace node with child
                if(previous.left == current):
                    previous.left = child
                else:
                    previous.right = child
                current = None
            # node has two children
            else:
                parent = None
                successor = current.right
                # find the successor node from the right subtree
                while(successor.left is not None):
                    parent = successor
                    successor = successor.left
                # successor's parent is not root
                if(parent is not None):
                    parent.left = successor.right
                # successor's parent is the root
                else:
                    current.right = successor.right
                # copy successor data to current node
                current.data = successor.data
                successor = None

    # delete all nodes from the BST
    def clear(self):
        while(not self.empty()):
            self.delete(self.__root.data)

    # return data from root node
    def root(self):
        if(self.__root is None):
            return None
        return self.__root.data

    # return node if found
    def get(self, data, current=None):
        if(self.empty()):
            return None
        # initial case
        if(current is None):
            self.get(data, self.__root)
        # look in left subtree
        elif(current.data > data):
            if(current.left is None):
                return None
            else:
                return self.get(data, current.left)
        # look in right subtree
        elif(current.data < data):
            if(current.right is None):
                return None
            else:
                return self.get(data, current.right)
        # node is found
        else:
            return current

   # return true if empty list
    def empty(self):
        return self.__root is None

    # return size of BST
    def size(self, current=None):
        if(self.empty()):
            return 0
        # initial case
        elif(current is None):
            return self.size(self.__root)
        size = 1
        # get size of left subtree
        if(current.left is not None):
            size += self.size(current.left)
        # get size of right subtree
        if(current.right is not None):
            size += self.size(current.right)
        return size

    # return height of BST
    def height(self, current=None):
        if(self.empty()):
            return 0
        # initial case
        elif(current is None):
            return self.height(self.__root)
        left_height = 0
        right_height = 0
        # base case
        if(current.left is None and current.right is None):
            return 1
        # get height of left sub tree
        if(current.left is not None):
            left_height = self.height(current.left)
        # get height of right subtree
        if(current.right is not None):
            right_height = self.height(current.right)
        # return greater height value
        if(left_height > right_height):
            return left_height + 1
        else:
            return right_height + 1

    # print BST inorder, preorder or postorder
    def print(self, order='inorder'):
        if(order == 'inorder'):
            print_list(inorder(self.__root))
        elif(order == 'preorder'):
            print_list(preorder(self.__root))
        else:
            print_list(postorder(self.__root))
