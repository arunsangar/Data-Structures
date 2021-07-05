from helper import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x, loc):
        if(loc < 0):
            print('Error: Cannot insert, undefined location')
            return
        node = Node(x)
        if(loc == 0):
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            counter = 0
            while(counter < loc - 1 and temp != None):
                temp = temp.next
                counter += 1
            if(temp == None):
                print('Cannot insert, location > size')
            else:
                node.next = temp.next
                temp.next = node

    def prepend(self, x):
        self.insert(x, 0)

    def append(self, x):
        if(self.head == None):
            self.head = Node(x)
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(x)

    def delete(self, x):
        if(self.head == None):
            print('Cannot delete, empty list')
            return
        temp = self.head
        prev = self.head
        if(temp.data == x):
            self.head = temp.next
            temp = None
        else:
            while(temp != None and temp.data != x):
                prev = temp
                temp = temp.next
            if(temp == None):
                print('Cannot delete, node not found')
            else:
                prev.next = temp.next
                temp = None

    def clear(self):
        temp = self.head
        while(temp != None):
            self.head = temp.next
            temp = None
            temp = self.head

    def get_node(self, x):
        if(self.head == None):
            return None
        temp = self.head
        while (temp != None and temp.data != x):
            temp = temp.next
        return temp

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
            print(temp.data)
            temp = temp.next
