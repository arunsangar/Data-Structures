from helper import Node


class LinkedList:
    def __init__(self):
        self.head = None

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
            temp = self.head
            counter = 0
            # find insertion point
            while(counter < loc - 1 and temp != None):
                temp = temp.next
                counter += 1
            # insert node if location was found
            if(temp != None):
                node.next = temp.next
                temp.next = node

    def prepend(self, x):
        # insert at front of list
        node = Node(x)
        node.next = self.head
        self.head = node

    def append(self, x):
        # empty list
        if(self.head == None):
            self.head = Node(x)
        # insert at back of list
        else:
            temp = self.head
            # get the last node
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(x)

    def delete(self, x):
        # empty list
        if(self.head == None):
            return
        temp = self.head
        prev = self.head
        # delete first node (head)
        if(temp.data == x):
            self.head = temp.next
        else:
            # find node set for deletion
            while(temp != None and temp.data != x):
                prev = temp
                temp = temp.next
            # delete the node if it was found
            if(temp != None):
                prev.next = temp.next

    def clear(self):
        temp = self.head
        while(temp != None):
            self.head = temp.next
            temp = self.head

    def get_node(self, x):
        # empty list
        if(self.head == None):
            return None
        temp = self.head
        # find the node
        while (temp != None and temp.data != x):
            temp = temp.next
        return temp

    def is_empty(self):
        if(self.head == None):
            return True
        return False

    def get_size(self):
        counter = 0
        temp = self.head
        while(temp != None):
            temp = temp.next
            counter += 1
        return counter

    def print(self):
        temp = self.head
        while(temp != None):
            if(temp.next != None):
                print(temp.data, end='->')
            else:
                print(temp.data)
            temp = temp.next
