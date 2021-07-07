from helper import TreeNode


class BSTIterative:

    def __init__(self):
        self.__root = None

    # insert specified node in the BST
    def insert(self, x):
        # empty BST
        if(self.__root == None):
            self.__root = TreeNode(x)
        # one or more nodes exist in BST
        else:
            temp = self.__root
            prev = None
            # find insertion point, return if duplicate
            while(temp != None):
                prev = temp
                if(temp.data == x):
                    return
                elif(temp.data > x):
                    temp = temp.left
                else:
                    temp = temp.right
            # insert node into left or right child
            if(prev.data > x):
                prev.left = TreeNode(x)
            else:
                prev.right = TreeNode(x)

    # delete specified node from the BST
    def delete(self, x):
        # empty BST
        if(self.__root == None):
            return
        temp = self.__root
        prev = None
        # find node set for deletion
        while(temp != None and temp.data != x):
            prev = temp
            if(temp.data > x):
                temp = temp.left
            else:
                temp = temp.right
        # node not found
        if(temp == None):
            return
        # node has at most one child
        if(temp.left == None or temp.right == None):
            child = None
            # choose child to replace current node
            if(temp.left == None):
                child = temp.right
            else:
                child = temp.left
            # node is root
            if(prev == None):
                self.__root = child
                return
            # replace node with child
            if(temp == prev.left):
                prev.left = child
            else:
                prev.right = child
        # node has two children
        else:
            parent = None
            successor = temp.right
            # find the successor node from the right subtree
            while(successor.left != None):
                parent = successor
                successor = successor.left
            # successor's parent is not root
            if(parent != None):
                parent.left = successor.right
            # successor's parent is the root
            else:
                temp.right = successor.right
            temp.data = successor.data

    # delete all nodes from the BST
    def clear(self):
        temp = self.__root
        while(temp != None):
            self.delete(temp.data)
            temp = self.__root

    # return data from root node
    def top(self):
        if(self.__root == None):
            return None
        return self.__root.data

    # return node if found
    def get(self, x):
        # empty BST
        if(self.__root == None):
            return None
        temp = self.__root
        # find the node
        while (temp != None and temp.data != x):
            if(temp.data == x):
                return temp
            elif(temp.data > x):
                temp = temp.left
            else:
                temp = temp.right
        # node was not found
        return None

    # return true if BST is empty
    def is_empty(self):
        if(self.__root == None):
            return True
        return False

    # print BST inorder, preorder or postorder
    def print(self, order='inorder'):
        data = []
        # select order type
        if(order == 'inorder'):
            data = self.inorder()
        elif(order == 'preorder'):
            data = self.preorder()
        else:
            data = self.postorder()
        # print ordered list
        while(data != []):
            if(len(data) > 1):
                print(data.pop(), end='->')
            else:
                print(data.pop())

    # return list of nodes inorder
    def inorder(self):
        # inorder - left, root, right
        stack = []
        data = []
        temp = self.__root
        while(stack != [] or temp != None):
            # traverse left, as far as possible
            if(temp != None):
                stack.append(temp)
                temp = temp.left
            # add root to ordered list and move to right child
            else:
                temp = stack.pop()
                data.insert(0, temp.data)
                temp = temp.right
        return data

    # return list of nodes preorder
    def preorder(self):
        # preorder - root, left, right
        stack = []
        data = []
        stack.append(self.__root)
        while(stack != []):
            temp = stack.pop()
            # add root to front of ordered list
            data.insert(0, temp.data)
            # add right child to stack
            if(temp.right != None):
                stack.append(temp.right)
            # add left child to stack
            if(temp.left != None):
                stack.append(temp.left)
        return data

    # return list of nodes postorder
    def postorder(self):
        # postorder - left, right, root
        stack = []
        data = []
        stack.append(self.__root)
        while(stack != []):
            temp = stack.pop()
            # add root to back of ordered list
            data.append(temp.data)
            # add left child to stack
            if(temp.left != None):
                stack.append(temp.left)
            # add right child to stack
            if(temp.right != None):
                stack.append(temp.right)
        return data
