from Utilities.nodes import Node
from Utilities.make_list import forward
from Utilities.make_list import backward
from Utilities.helper import print_list


class Queue:

    def __init__(self):
        self.__front = None
        self.__back = None

    # insert node to back of queue
    def enqueue(self, x):
        # empty queue
        if(self.empty()):
            self.__front = Node(x)
            self.__back = self.__front
        # insert at back of queue
        else:
            self.__back.next = Node(x)
            self.__back = self.__back.next

    # remove and return front node
    def dequeue(self):
        # empty queue
        if(self.empty()):
            return None
        # queue has at least one node
        else:
            temp = self.__front
            self.__front = temp.next
            # if popping last remaining node
            if(self.__back == temp):
                self.__back = None
            return temp.data

    # delete specified node from the queue
    # does not delete if node does not exist
    def delete(self, data):
        # empty queue
        if(self.empty()):
            return
        temp = self.__front
        # delete first node (front)
        if(temp.data == data):
            self.__front = temp.next
            if(self.__back == temp):
                self.__back = None
            temp = None
        else:
            # find node set for deletion
            while(temp is not None and temp.data != data):
                prev = temp
                temp = temp.next
            # delete the node if it was found
            if(temp is not None):
                prev.next = temp.next
                if(self.__back == temp):
                    self.__back = prev
                temp = None

    # delete all nodes from the queue
    def clear(self):
        while(not self.empty()):
            temp = self.__front
            self.__front = temp.next
            temp = None
        self.__back = None

    # return data from front node
    def front(self):
        if(self.empty()):
            return None
        return self.__front.data

    # return node if found
    def get(self, data):
        # find the node
        temp = self.__front
        while (temp is not None and temp.data != data):
            temp = temp.next
        return temp

    # return true if queue is empty
    def empty(self):
        return self.__front is None

    # return size of queue
    def size(self):
        counter = 0
        temp = self.__front
        while(temp is not None):
            temp = temp.next
            counter += 1
        return counter

    # print queue forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(forward(self.__front))
        else:
            print_list(backward(self.__front))
