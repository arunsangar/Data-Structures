from helper import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, x):
        # empty queue
        if(self.front == None):
            self.front = Node(x)
            self.back = self.front
        # insert at back of queue
        else:
            self.back.next = Node(x)
            self.back = self.back.next

    def pop(self):
        # empty queue
        if(self.front == None):
            return None
        # queue has at least one node
        else:
            temp = self.front
            self.front = temp.next
            # only one node in queue
            if(self.back == temp):
                self.back = None
            return temp.data

    def clear(self):
        while(self.front != None):
            self.pop()

    def top(self):
        if(self.front == None):
            return None
        return self.front.data

    def is_empty(self):
        if(self.front == None):
            return True
        return False

    def get_size(self):
        temp = self.front
        counter = 0
        while(temp != None):
            temp = temp.next
            counter += 1
        return counter

    def print(self):
        temp = self.front
        while(temp != None):
            if(temp.next != None):
                print(temp.data, end='->')
            else:
                print(temp.data)
            temp = temp.next
