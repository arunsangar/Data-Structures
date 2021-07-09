from Utilities.nodes import Node
from Utilities.make_list import forward
from Utilities.make_list import backward
from Utilities.helper import print_list


class Queue:

    def __init__(self):
        self.__front = None
        self.__back = None

    # push node to back of queue
    def push(self, x):
        # empty queue
        if(self.__front == None):
            self.__front = Node(x)
            self.__back = self.__front
        # insert at back of queue
        else:
            self.__back.next = Node(x)
            self.__back = self.__back.next

    # pop front node and return data
    def pop(self):
        # empty queue
        if(self.__front == None):
            return None
        # queue has at least one node
        else:
            temp = self.__front
            self.__front = temp.next
            # if popping last remaining node
            if(self.__back == temp):
                self.__back = None
            return temp.data

    # delete all nodes from the queue
    def clear(self):
        while(self.__front != None):
            self.pop()

    # return data from front node
    def top(self):
        if(self.__front == None):
            return None
        return self.__front.data

    # return true if queue is empty
    def is_empty(self):
        if(self.__front == None):
            return True
        return False

    # return size of queue
    def size(self):
        temp = self.__front
        counter = 0
        while(temp != None):
            temp = temp.next
            counter += 1
        return counter

    # print queue forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(forward(self.__front))
        else:
            print_list(backward(self.__front))
