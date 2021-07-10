from Utilities.nodes import Node
from Utilities.make_list import circular
from Utilities.helper import print_list


class CircularLinkedList:

    def __init__(self):
        self.__last = None

    # insert specified node at desired location
    # does not insert if location > size
    def insert(self, data, loc=0):
        size = self.size()
        # undefined location
        if(loc < 0 or loc > size):
            return
        # insert at front of list
        if(loc == 0):
            self.prepend(data)
        # insert at back of list
        elif(loc == size):
            self.append(data)
        # insert at specified location
        else:
            node = Node(data)
            temp = self.__last.next
            counter = 0
            # find insertion point
            while(counter < loc - 1):
                temp = temp.next
                counter += 1
            # insert node
            node.next = temp.next
            temp.next = node

    # insert node at front of list
    def prepend(self, data):
        node = Node(data)
        if(self.empty()):
            self.__last = node
            node.next = node
        else:
            node.next = self.__last.next
            self.__last.next = node

    # insert node at back of list
    def append(self, data):
        # empty list
        if(self.empty()):
            self.prepend(data)
        # find last node and insert
        else:
            node = Node(data)
            node.next = self.__last.next
            self.__last.next = node
            self.__last = node

    # delete specified node from the list
    # does not delete if node does not exist
    def delete(self, data):
        # empty list
        if(self.empty()):
            return
        temp = self.__last.next
        if(temp is temp.next):
            self.__last = None
        elif(temp.data == data):
            self.__last.next = temp.next
            temp = None
        else:
            # find node set for deletion
            while(temp.data != data):
                prev = temp
                temp = temp.next
                if(temp is self.__last.next):
                    break
            # delete the node
            if(temp == self.__last):
                prev.next = temp.next
                self.__last = prev
                temp = None
            elif(temp.data == data):
                prev.next = temp.next
                temp = None

    # delete all nodes from the list
    def clear(self):
        while(not self.empty()):
            self.delete(self.__last.data)

    # return data from head node
    def head(self):
        if(self.empty()):
            return None
        else:
            return self.__last.next.data

    # return node if found
    def get(self, data):
        if(self.empty()):
            return None
        # find the node
        temp = self.__last.next
        while (temp.data != data):
            temp = temp.next
            if(temp is self.__last.next):
                temp = None
                break
        return temp

    # return true if list is empty
    def empty(self):
        return self.__last is None

    # return size of list
    def size(self):
        if(self.empty()):
            return 0
        counter = 1
        temp = self.__last.next
        while(temp is not self.__last):
            temp = temp.next
            counter += 1
        return counter

    # print list forward or backward
    def print(self, order='forward'):
        if(order == 'forward'):
            print_list(circular(self.__last))
