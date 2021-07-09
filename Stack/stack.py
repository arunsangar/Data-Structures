from Utilities.nodes import Node
from Utilities.make_list import forward
from Utilities.make_list import backward
from Utilities.helper import print_list


class Stack:

    def __init__(self):
        self.__head = None

    # push node to top of stack
    def push(self, x):
        temp = Node(x)
        temp.next = self.__head
        self.__head = temp

    # remove and return top node
    def pop(self):
        # empty stack
        if(self.__head == None):
            return None
        # stack has at least one node
        temp = self.__head
        self.__head = temp.next
        return temp

    # delete all nodes from the stack
    def clear(self):
        while(self.__head != None):
            self.pop()

    # return data from front node
    def top(self):
        if(self.__head == None):
            return None
        return self.__head.data

    # return true if stack is empty
    def empty(self):
        if(self.__head == None):
            return True
        return False

    # return size of stack
    def size(self):
        counter = 0
        temp = self.__head
        while(temp != None):
            temp = temp.next
            counter += 1
        return counter

    # print stack forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(forward(self.__head))
        else:
            print_list(backward(self.__head))
