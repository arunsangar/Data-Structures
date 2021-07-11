from Utilities.nodes import PQNode
from Utilities.make_list import priority
from Utilities.helper import print_list
from math import ceil


class PriorityQueue:

    def __init__(self):
        self.__queue = []

    def enqueue(self, data, priority):
        self.__queue.append(PQNode(data, priority))
        self.__percolate_up(self.size()-1)

    def dequeue(self):
        if(self.empty()):
            return None
        temp = self.__queue.pop(0)
        self.__percolate_down(0)
        return temp

    def delete(self, data):
        index = self.__get_index(data)
        if(index is not None):
            self.__queue[index] = self.__queue[self.size()-1]
            self.__queue.pop()
            self.__percolate_down(index)

    def clear(self):
        while(self.__queue != []):
            self.__queue.pop()

    def front(self):
        if(self.empty()):
            return None
        return self.__queue[0].data

    def get(self, data):
        if(self.empty()):
            return None
        # utilize stack to track unvisited nodes
        stack = []
        stack.append(0)
        size = self.size()-1
        # find the node
        while(stack != []):
            index = stack.pop()
            if(data != self.__queue[index].data):
                left = (index*2)+1
                right = (index*2)+2
                if(left <= size):
                    stack.append(left)
                if(right <= size):
                    stack.append(right)
            else:
                return self.__queue[index]
        return None

    def empty(self):
        return self.__queue == []

    def size(self):
        return len(self.__queue)

    def print(self):
        print_list(priority(self.__queue))

    def __percolate_up(self, index):
        while(index != 0):
            child = self.__queue[index]
            parent = self.__queue[ceil((index-2)/2)]
            if(child.priority > parent.priority):
                self.__queue[index] = parent
                self.__queue[ceil((index-2)/2)] = child
                index = ceil((index-2)/2)
            else:
                break

    def __percolate_down(self, index):
        size = self.size()
        while((index*2)+2 < size):
            parent = self.__queue[index]
            left = self.__queue[(index*2)+1]
            if((index*2)+1 == size):
                child = self.__queue[(index*2)+1]
            elif(left.priority > self.__queue[(index*2)+2].priority):
                child = self.__queue[(index*2)+1]
            else:
                child = self.__queue[(index*2)+2]
            if(parent.priority < child.priority):
                if(child is left):
                    self.__queue[index] = left
                    self.__queue[(index*2)+1] = parent
                    index = (index*2)+1
                else:
                    self.__queue[index] = self.__queue[(index*2)+2]
                    self.__queue[(index*2)+2] = parent
                    index = (index*2)+2
            else:
                break

    def __get_index(self, data):
        if(self.empty()):
            return None
        # utilize stack to track unvisited nodes
        stack = []
        stack.append(0)
        size = self.size()-1
        # find the node
        while(stack != []):
            index = stack.pop()
            if(data != self.__queue[index].data):
                left = (index*2)+1
                right = (index*2)+2
                if(left <= size):
                    stack.append(left)
                if(right <= size):
                    stack.append(right)
            else:
                return index
        return None
