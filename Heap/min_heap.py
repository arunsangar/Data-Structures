from nodes import HeapNode


class MinHeap:

    def __init__(self):
        self.__root = None

    # insert specified node in the heap
    def insert(self, x, current=None, traverse=''):
        if(traverse == '' and current == None):
            # insert into empty heap
            if(self.__root == None):
                self.__root = HeapNode(x, None)
                return
            # get binary representation of heap size + 1
            else:
                traverse = self.__get_bin(self.size() + 1)
                self.insert(x, self.__root, traverse[1:])
        # insert left if traversal is complete
        # traverse down left subtree if not
        elif(traverse[0] == '0'):
            if(len(traverse) == 1):
                current.left = HeapNode(x, current)
                self.__percolate_up(current.left)
            else:
                self.insert(x, current.left, traverse[1:])
        # insert right if traversal is complete
        # traverse down right subtree if not
        elif(traverse[0] == '1'):
            if(len(traverse) == 1):
                current.right = HeapNode(x, current)
                self.__percolate_up(current.right)
            else:
                self.insert(x, current.right, traverse[1:])

    # delete specified node from the list
    # does not delete if node does not exist
    def delete(self, x):
        # check if specified node exists
        temp = self.get(x)
        if(temp == None):
            return
        else:
            # get the last node in heap and swap
            last_node = self.__get_last()
            self.__swap(temp, last_node)
            # remove the last node from the heap
            if(last_node == last_node.parent.left):
                last_node.parent.left = None
            else:
                last_node.parent.right = None
            # preserve max heap
            self.__percolate_down(temp)

    # return node if found
    def get(self, x):
        # empty heap
        if(self.__root == None):
            return None
        # utilize stack to track unvisited nodes
        stack = []
        stack.append(self.__root)
        # find the node
        while(stack != []):
            temp = stack.pop()
            if(x > temp.data):
                if(temp.left != None):
                    stack.append(temp.left)
                if(temp.right != None):
                    stack.append(temp.right)
            elif(x == temp.data):
                return temp
        return None

    # return size of heap
    def size(self, current=None):
        # initial recursive call
        if(current == None):
            if(self.__root == None):
                return 0
            else:
                return self.size(self.__root)
        # get size of left and right subtree
        size = 0
        if(current.left != None):
            size += self.size(current.left)
        if(current.right != None):
            size += self.size(current.right)
        # return size of subtrees + current node
        return size + 1

    # return height of heap
    def height(self, current=None):
        # initial recursive call
        if(current == None):
            if(self.__root == None):
                return 0
            else:
                return self.height(self.__root)
        # get height of left and right subtrees
        height_left = 0
        height_right = 0
        if(current.left != None):
            height_left = self.height(current.left)
        if(current.right != None):
            height_right = self.height(current.right)
        # return the maximum of the two subtrees + 1
        if(height_left > height_right):
            return height_left + 1
        else:
            return height_right + 1

    # print heap inorder, preorder or postorder
    def print(self, order='inorder'):
        data = []
        # select order type
        if(order == 'inorder'):
            data = self.inorder(self.__root)
        elif(order == 'preorder'):
            data = self.preorder(self.__root)
        else:
            data = self.postorder(self.__root)
        # print ordered list
        while(data != []):
            if(len(data) > 1):
                print(data.pop(0), end='->')
            else:
                print(data.pop(0))

    # return list of nodes inorder
    def inorder(self, current):
        # inorder - left, root, right
        if(current == None):
            return None
        data = []
        # traverse left subtree
        temp = self.inorder(current.left)
        if(temp != None):
            data += temp
        # add root to ordered list
        data.append(current.data)
        # traverse right subtree
        temp = self.inorder(current.right)
        if(temp != None):
            data += temp
        return data

    # return list of nodes preorder
    def preorder(self, current):
        # preorder - root, left, right
        if(current == None):
            return None
        data = []
        # add root to ordered list
        data.append(current.data)
        # traverse left subtree
        temp = self.preorder(current.left)
        if(temp != None):
            data += temp
        # traverse right subtree
        temp = self.preorder(current.right)
        if(temp != None):
            data += temp
        return data

    # return list of nodes postorder
    def postorder(self, current):
        # postorder - left, right, root
        if(current == None):
            return None
        data = []
        # traverse left subtree
        temp = self.postorder(current.left)
        if(temp != None):
            data += temp
        # traverse right subtree
        temp = self.postorder(current.right)
        if(temp != None):
            data += temp
        # add root to ordered list
        data.append(current.data)
        return data

    # used after insertion to preserve max heap
    def __percolate_up(self, current):
        # current is root node
        if(current.parent == None):
            return
        # swap if child is less than parent
        if(current.data < current.parent.data):
            self.__swap(current.parent, current)
        # recurse up the heap
        self.__percolate_up(current.parent)

    # used after deletion to preserve max heap
    def __percolate_down(self, current):
        # current is a leaf node (heap is left filled)
        if(current.left == None):
            return
        # swap if parent is greater than child
        if(current.right == None or current.left.data < current.right.data):
            self.__swap(current, current.left)
            self.__percolate_down(current.left)
        else:
            self.__swap(current, current.right)
            self.__percolate_down(current.right)

    # used in deletion to get the last node
    def __get_last(self, current=None, traverse=''):
        if(self.__root == None):
            return None
        if(traverse == '' and current == None):
            traverse = self.__get_bin(self.size())
            return self.__get_last(self.__root, traverse[1:])
        # insert left if traversal is complete
        # traverse down left subtree if not
        elif(traverse[0] == '0'):
            if(len(traverse) == 1):
                return current.left
            else:
                return self.__get_last(current.left, traverse[1:])
        # insert right if traversal is complete
        # traverse down right subtree if not
        elif(traverse[0] == '1'):
            if(len(traverse) == 1):
                return current.right
            else:
                return self.__get_last(current.right, traverse[1:])

    # swap data of child and parent node
    def __swap(self, parent, child):
        temp = parent.data
        parent.data = child.data
        child.data = temp

    # return binary representation of integer
    def __get_bin(self, x):
        return format(x, 'b')
