from helper import TreeNode


class BSTIterative:
    def __init__(self):
        self.root = None

    def insert(self, x):
        # empty BST
        if(self.root == None):
            self.root = TreeNode(x)
        # 1 or more nodes exist in BST
        else:
            temp = self.root
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

    def delete(self, x):
        # empty BST
        if(self.root == None):
            return
        temp = self.root
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
                self.root = child
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

    def clear(self):
        temp = self.root
        while(temp != None):
            self.delete(temp.data)
            temp = self.root

    def top(self):
        if(self.root == None):
            return None
        return self.root.data

    def get(self, x):
        # empty BST
        if(self.root == None):
            return None
        temp = self.root
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

    def is_empty(self):
        if(self.root == None):
            return True
        return False

    def print(self, order='inorder'):
        data = []
        if(order == 'inorder'):
            data = self.inorder()
        elif(order == 'preorder'):
            data = self.preorder()
        else:
            data = self.postorder()
        while(data != []):
            if(len(data) > 1):
                print(data.pop(), end='->')
            else:
                print(data.pop())

    def inorder(self):
        stack = []
        data = []
        temp = self.root
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

    def preorder(self):
        stack = []
        data = []
        stack.append(self.root)
        while(stack != []):
            temp = stack.pop()
            # add root to ordered list
            data.insert(0, temp.data)
            # add right child to stack
            if(temp.right != None):
                stack.append(temp.right)
            # add left child to stack
            if(temp.left != None):
                stack.append(temp.left)
        return data

    def postorder(self):
        stack = []
        data = []
        stack.append(self.root)
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
