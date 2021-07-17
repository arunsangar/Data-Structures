from Utilities.nodes import AVLTreeNode
from Utilities.make_list import inorder
from Utilities.make_list import preorder
from Utilities.make_list import postorder
from Utilities.helper import print_list


class AVLTree:

    def __init__(self):
        self.__root = None

    def insert(self, data):
        if(self.empty()):
            self.__root = AVLTreeNode(data, None)
        else:
            current = self.__root
            prev = None
            while(current is not None):
                if(data < current.data):
                    prev = current
                    current = current.left
                elif(data > current.data):
                    prev = current
                    current = current.right
                else:
                    return
            if(data < prev.data):
                prev.left = AVLTreeNode(data, prev)
                current = prev.left
            else:
                prev.right = AVLTreeNode(data, prev)
                current = prev.right
            self.__update_height(current)
            node, balance = self.__check_balance(current)
            if(balance is None):
                return
            # left left - right rotate
            if(balance > 1 and data < node.left.data):
                self.__right_rotate(node)
            # right right - left rotate
            elif(balance < -1 and data > node.right.data):
                self.__left_rotate(node)
            # left right - left right rotate
            elif(balance > 1 and data > node.left.data):
                self.__left_rotate(node.left)
                self.__right_rotate(node)
            # right left - right left rotate
            elif(balance < -1 and data < node.right.data):
                self.__right_rotate(node.right)
                self.__left_rotate(node)

    # def delete(self, data):

    # def clear(self):

    def root(self):
        if(self.empty()):
            return None
        return self.__root.data

    def get(self, data):
        if(self.empty()):
            return None
        current = self.__root
        while(current is not None):
            if(data < current.data):
                current = current.left
            elif(data > current.data):
                current = current.right
            else:
                return current
        return None

    def empty(self):
        return self.__root is None

    def size(self):
        if(self.empty()):
            return 0
        visited = []
        children = []
        children.append(self.__root)
        while(children != []):
            current = children.pop()
            if(current.left is not None):
                children.append(current.left)
            if(current.right is not None):
                children.append(current.right)
            visited.append(current)
        return len(visited)

    def height(self):
        if(self.empty()):
            return 0
        return self.__root.height

    # print AVL Tree inorder, preorder or postorder
    def print(self, order='inorder'):
        if(order == 'inorder'):
            print_list(inorder(self.__root))
        elif(order == 'preorder'):
            print_list(preorder(self.__root))
        else:
            print_list(postorder(self.__root))

    def __update_height(self, current):
        if(current is None):
            return
        while(current is not None):
            if(current.left is None):
                left = 0
            else:
                left = current.left.height
            if(current.right is None):
                right = 0
            else:
                right = current.right.height
            current.height = 1 + max(left, right)
            current = current.parent

    def __check_balance(self, current):
        if(current is None):
            return
        while(current is not None):
            if(current.left is None):
                left = 0
            else:
                left = current.left.height
            if(current.right is None):
                right = 0
            else:
                right = current.right.height
            if(left - right > 1 or left - right < -1):
                return current, left - right
            current = current.parent
        return None, None

    def __left_rotate(self, z):
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        y.parent = z.parent
        z.parent = y
        if(x is not None):
            x.parent = z
        if(y.parent is None):
            self.__root = y
        elif(y.parent.left == z):
            y.parent.left = y
        else:
            y.parent.right = y
        self.__update_height(z)

    def __right_rotate(self, z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x
        y.parent = z.parent
        z.parent = y
        if(x is not None):
            x.parent = z
        if(y.parent is None):
            self.__root = y
        elif(y.parent.left == z):
            y.parent.left = y
        else:
            y.parent.right = y
        self.__update_height(z)
