from helper import Node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if(self.head != None):
            temp = self.head
            self.head = temp.next
            return temp.data

    def clear(self):
        while(self.head != None):
            self.pop()

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
