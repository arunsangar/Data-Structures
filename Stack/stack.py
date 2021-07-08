from nodes import Node


class Stack:

    def __init__(self):
        self.__head = None

    # push node to front of stack
    def push(self, x):
        temp = Node(x)
        temp.next = self.__head
        self.__head = temp

    # pop front node and return data
    def pop(self):
        # empty stack
        if(self.__head == None):
            return None
        # stack has at least one node
        temp = self.__head
        self.__head = temp.next
        return temp.data

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
    def is_empty(self):
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

    # print stack front to back
    def print(self):
        temp = self.__head
        while(temp != None):
            if(temp.next != None):
                print(temp.data, end='->')
            else:
                print(temp.data)
            temp = temp.next
