from Utilities.nodes import Node
from Utilities.make_list import forward
from Utilities.make_list import backward
from Utilities.helper import print_list


class Stack:

    def __init__(self):
        self.__top = None

    # push node to top of stack
    def push(self, data):
        temp = Node(data)
        temp.next = self.__top
        self.__top = temp

    # remove and return top node
    def pop(self):
        # empty stack
        if(self.empty()):
            return None
        # stack has at least one node
        temp = self.__top
        self.__top = temp.next
        return temp

    # delete specified node from the stack
    # does not delete if node does not exist
    def delete(self, data):
        # empty list
        if(self.empty()):
            return
        temp = self.__top
        # delete first node (top)
        if(temp.data == data):
            self.__top = temp.next
            temp = None
        else:
            # find node set for deletion
            while(temp is not None and temp.data != data):
                prev = temp
                temp = temp.next
            # delete the node if it was found
            if(temp is not None):
                prev.next = temp.next
                temp = None

    # delete all nodes from the stack
    def clear(self):
        while(not self.empty()):
            temp = self.__top
            self.__top = temp.next
            temp = None

    # return data from front node
    def top(self):
        if(self.empty()):
            return None
        return self.__top.data

    # return node if found
    def get(self, data):
        # find the node
        temp = self.__top
        while (temp is not None and temp.data != data):
            temp = temp.next
        return temp

    # return true if stack is empty
    def empty(self):
        return self.__top is None

    # return size of stack
    def size(self):
        counter = 0
        temp = self.__top
        while(temp is not None):
            temp = temp.next
            counter += 1
        return counter

    # print stack forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(forward(self.__top))
        else:
            print_list(backward(self.__top))
