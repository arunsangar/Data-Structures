from Utilities.nodes import TreeNode
from Utilities.make_list import inorder
from Utilities.make_list import preorder
from Utilities.make_list import postorder
from Utilities.helper import print_list


class BSTIterative:

    def __init__(self):
        self.__root = None

    # insert specified node in the BST
    def insert(self, data):
        # empty BST
        if(self.empty()):
            self.__root = TreeNode(data)
        # one or more nodes exist in BST
        else:
            temp = self.__root
            prev = None
            # find insertion point, return if duplicate
            while(temp is not None):
                prev = temp
                if(temp.data == data):
                    return
                elif(temp.data > data):
                    temp = temp.left
                else:
                    temp = temp.right
            # insert node into left or right child
            if(prev.data > data):
                prev.left = TreeNode(data)
            else:
                prev.right = TreeNode(data)

    # delete specified node from the BST
    def delete(self, data):
        # find node set for deletion
        temp = self.__root
        prev = None
        while(temp is not None and temp.data != data):
            prev = temp
            if(temp.data > data):
                temp = temp.left
            else:
                temp = temp.right
        # node not found
        if(temp is None):
            return
        # node has at most one child
        if(temp.left is None or temp.right is None):
            child = None
            # choose child to replace current node
            if(temp.left is None):
                child = temp.right
            else:
                child = temp.left
            # node is root
            if(prev is None):
                self.__root = child
                temp = None
                return
            # replace node with child
            if(temp == prev.left):
                prev.left = child
            else:
                prev.right = child
            temp = None
        # node has two children
        else:
            successor = temp.right
            parent = None
            # find the successor node from the right subtree
            while(successor.left is not None):
                parent = successor
                successor = successor.left
            # successor's parent is not root
            if(parent is not None):
                parent.left = successor.right
            # successor's parent is the root
            else:
                temp.right = successor.right
            temp.data = successor.data
            successor = None

    # delete all nodes from the BST
    def clear(self):
        while(not self.empty()):
            self.delete(self.__root.data)

    # return data from root node
    def root(self):
        if(self.empty()):
            return None
        return self.__root.data

    # return node if found
    def get(self, x):
        temp = self.__root
        # find the node
        while (temp is not None and temp.data != x):
            if(temp.data == x):
                return temp
            elif(temp.data > x):
                temp = temp.left
            else:
                temp = temp.right
        # node was not found
        return None

    # return true if BST is empty
    def empty(self):
        return self.__root is None

    def size(self):
        if(self.empty()):
            return 0
        size = 0
        stack = []
        stack.append(self.__root)
        while(stack != []):
            temp = stack.pop()
            if(temp.left is not None):
                stack.append(temp.left)
            if(temp.right is not None):
                stack.append(temp.right)
            size += 1
        return size

    def height(self):
        if(self.empty()):
            return 0
        height = 0
        queue = []
        queue.append(self.__root)
        while(queue != []):
            level_size = len(queue)
            height += 1
            while(level_size > 0):
                temp = queue.pop(0)
                if(temp.left is not None):
                    queue.append(temp.left)
                if(temp.right is not None):
                    queue.append(temp.right)
                level_size -= 1
        return height

    # print BST inorder, preorder or postorder
    def print(self, order='inorder'):
        # select order type
        if(order == 'inorder'):
            print_list(inorder(self.__root))
        elif(order == 'preorder'):
            print_list(preorder(self.__root))
        else:
            print_list(postorder(self.__root))
