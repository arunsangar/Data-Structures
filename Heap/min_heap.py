from Utilities.nodes import HeapNode
from Utilities.make_list import inorder
from Utilities.make_list import preorder
from Utilities.make_list import postorder
from Utilities.helper import print_list


class MinHeap:

    def __init__(self):
        self.__root = None

    # insert specified node in the heap
    def insert(self, data, current=None, traverse=''):
        if(traverse == '' and current is None):
            # insert into empty heap
            if(self.empty()):
                self.__root = HeapNode(data, None)
                return
            # get binary representation of heap size + 1
            else:
                traverse = self.__get_bin(self.size() + 1)
                self.insert(data, self.__root, traverse[1:])
        # insert left if traversal is complete
        # traverse down left subtree if not
        elif(traverse[0] == '0'):
            if(len(traverse) == 1):
                current.left = HeapNode(data, current)
                self.__percolate_up(current.left)
            else:
                self.insert(data, current.left, traverse[1:])
        # insert right if traversal is complete
        # traverse down right subtree if not
        elif(traverse[0] == '1'):
            if(len(traverse) == 1):
                current.right = HeapNode(data, current)
                self.__percolate_up(current.right)
            else:
                self.insert(data, current.right, traverse[1:])

    # delete specified node from the list
    # does not delete if node does not exist
    def delete(self, data):
        # check if specified node exists
        temp = self.get(data)
        if(temp is None):
            return
        elif(self.size() == 1):
            self.__root = None
            temp = None
        else:
            # get the last node in heap and swap
            last_node = self.__get_last()
            self.__swap(temp, last_node)
            # remove the last node from the heap
            if(last_node == last_node.parent.left):
                last_node.parent.left = None
            else:
                last_node.parent.right = None
            last_node = None
            # preserve max heap
            self.__percolate_down(temp)

    # delete all nodes from the heap
    def clear(self):
        while(not self.empty()):
            self.delete(self.__root.data)

    # return data from root node
    def root(self):
        if(self.empty()):
            return None
        return self.__root.data

    # return node if found
    def get(self, data):
        # empty heap
        if(self.empty()):
            return None
        # utilize stack to track unvisited nodes
        stack = []
        stack.append(self.__root)
        # find the node
        while(stack != []):
            temp = stack.pop()
            if(data > temp.data):
                if(temp.left is not None):
                    stack.append(temp.left)
                if(temp.right is not None):
                    stack.append(temp.right)
            elif(data == temp.data):
                return temp
        return None

    # return true if empty list
    def empty(self):
        return self.__root is None

    # return size of heap
    def size(self, current=None):
        # initial recursive call
        if(current is None):
            if(self.empty()):
                return 0
            else:
                return self.size(self.__root)
        # get size of left and right subtree
        size = 0
        if(current.left is not None):
            size += self.size(current.left)
        if(current.right is not None):
            size += self.size(current.right)
        # return size of subtrees + current node
        return size + 1

    # return height of heap
    def height(self, current=None):
        # initial recursive call
        if(current is None):
            if(self.empty()):
                return 0
            else:
                return self.height(self.__root)
        # get height of left and right subtrees
        height_left = 0
        height_right = 0
        if(current.left is not None):
            height_left = self.height(current.left)
        if(current.right is not None):
            height_right = self.height(current.right)
        # return the maximum of the two subtrees + 1
        if(height_left > height_right):
            return height_left + 1
        else:
            return height_right + 1

    # print heap inorder, preorder or postorder
    def print(self, order='inorder'):
        if(order == 'inorder'):
            print_list(inorder(self.__root))
        elif(order == 'preorder'):
            print_list(preorder(self.__root))
        else:
            print_list(postorder(self.__root))

    # used after insertion to preserve max heap
    def __percolate_up(self, current):
        # current is root node
        if(current.parent is None):
            return
        # swap if child is less than parent
        if(current.data < current.parent.data):
            self.__swap(current.parent, current)
        # recurse up the heap
        self.__percolate_up(current.parent)

    # used after deletion to preserve max heap
    def __percolate_down(self, current):
        # current is a leaf node (heap is left filled)
        if(current.left is None):
            return
        # swap if parent is greater than child
        if(current.right is None or current.left.data < current.right.data):
            self.__swap(current, current.left)
            self.__percolate_down(current.left)
        else:
            self.__swap(current, current.right)
            self.__percolate_down(current.right)

    # used in deletion to get the last node
    def __get_last(self, current=None, traverse=''):
        if(self.empty()):
            return None
        if(traverse == '' and current is None):
            traverse = self.__get_bin(self.size())
            return self.__get_last(self.__root, traverse[1:])
        # insert left if traversal is complete
        # traverse down left subtree if not
        elif(traverse[0] == '0'):
            if(len(traverse) == 1):
                return current.left
            else:
                return self.__get_last(current.left, traverse[1:])
        # insert right if traversal is complete
        # traverse down right subtree if not
        elif(traverse[0] == '1'):
            if(len(traverse) == 1):
                return current.right
            else:
                return self.__get_last(current.right, traverse[1:])

    # swap data of child and parent node
    def __swap(self, parent, child):
        temp = parent.data
        parent.data = child.data
        child.data = temp

    # return binary representation of integer
    def __get_bin(self, x):
        return format(x, 'b')
