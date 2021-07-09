from Utilities.nodes import Node
from Utilities.make_list import forward
from Utilities.make_list import backward
from Utilities.helper import print_list


class LinkedList:

    def __init__(self):
        self.__head = None

    # insert specified node at desired location
    # does not insert if location > size
    def insert(self, x, loc):
        # undefined location
        if(loc < 0):
            return
        # insert at front of list
        if(loc == 0):
            self.prepend(x)
        # insert at specified location
        else:
            node = Node(x)
            temp = self.__head
            counter = 0
            # find insertion point
            while(counter < loc - 1 and temp != None):
                temp = temp.next
                counter += 1
            # insert node if location was found
            if(temp != None):
                node.next = temp.next
                temp.next = node

    # insert node at front of list
    def prepend(self, x):
        node = Node(x)
        node.next = self.__head
        self.__head = node

    # insert node at back of list
    def append(self, x):
        # empty list
        if(self.__head == None):
            self.__head = Node(x)
        # find last node and insert
        else:
            temp = self.__head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(x)

    # delete specified node from the list
    # does not delete if node does not exist
    def delete(self, x):
        # empty list
        if(self.__head == None):
            return
        temp = self.__head
        prev = self.__head
        # delete first node (head)
        if(temp.data == x):
            self.__head = temp.next
        else:
            # find node set for deletion
            while(temp != None and temp.data != x):
                prev = temp
                temp = temp.next
            # delete the node if it was found
            if(temp != None):
                prev.next = temp.next

    # delete all nodes from the list
    def clear(self):
        temp = self.__head
        while(temp != None):
            self.__head = temp.next
            temp = self.__head

    # return node if found
    def get(self, x):
        # empty list
        if(self.__head == None):
            return None
        # find the node
        temp = self.__head
        while (temp != None and temp.data != x):
            temp = temp.next
        return temp

    # return true if list is empty
    def empty(self):
        if(self.__head == None):
            return True
        return False

    # return size of list
    def size(self):
        counter = 0
        temp = self.__head
        while(temp != None):
            temp = temp.next
            counter += 1
        return counter

    # print list forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(forward(self.__head))
        else:
            print_list(backward(self.__head))
