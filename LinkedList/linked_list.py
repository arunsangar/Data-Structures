from Utilities.nodes import Node
from Utilities.make_list import forward
from Utilities.make_list import backward
from Utilities.helper import print_list


class LinkedList:

    def __init__(self):
        self.__head = None

    # insert specified node at desired location
    # does not insert if location > size
    def insert(self, data, loc=0):
        # undefined location
        if(loc < 0):
            return
        # insert at front of list
        if(loc == 0):
            self.prepend(data)
        # insert at specified location
        else:
            node = Node(data)
            temp = self.__head
            counter = 0
            # find insertion point
            while(counter < loc - 1 and temp is not None):
                temp = temp.next
                counter += 1
            # insert node if location was found
            if(temp is not None):
                node.next = temp.next
                temp.next = node

    # insert node at front of list
    def prepend(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head = node

    # insert node at back of list
    def append(self, data):
        # empty list
        if(self.empty()):
            self.__head = Node(data)
        # find last node and insert
        else:
            temp = self.__head
            while(temp.next is not None):
                temp = temp.next
            temp.next = Node(data)

    # delete specified node from the list
    # does not delete if node does not exist
    def delete(self, data):
        # empty list
        if(self.empty()):
            return
        temp = self.__head
        # delete first node (head)
        if(self.__head.data == data):
            self.__head = self.__head.next
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

    # delete all nodes from the list
    def clear(self):
        while(not self.empty()):
            temp = self.__head
            self.__head = temp.next
            temp = None

    # return data from head node
    def head(self):
        if(self.empty()):
            return None
        else:
            return self.__head.data

    # return node if found
    def get(self, data):
        # find the node
        temp = self.__head
        while (temp is not None and temp.data != data):
            temp = temp.next
        return temp

    # return true if list is empty
    def empty(self):
        return self.__head is None

    # return size of list
    def size(self):
        counter = 0
        temp = self.__head
        while(temp is not None):
            temp = temp.next
            counter += 1
        return counter

    # print list forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(forward(self.__head))
        else:
            print_list(backward(self.__head))
