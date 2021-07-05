from helper import TreeNode


class BinarySearchTree:
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

    def get_node(self, x):
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

    def print_inorder(self):
        stack = []
        temp = self.root
        while(stack != [] or temp != None):
            if(temp != None):
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                if(stack == [] and temp.right == None):
                    print(temp.data)
                else:
                    print(temp.data, end='->')
                temp = temp.right

    def print_preorder(self):
        stack = []
        stack.append(self.root)
        while(stack != []):
            temp = stack.pop()
            if(temp.right != None):
                stack.append(temp.right)
            if(temp.left != None):
                stack.append(temp.left)
            if(stack == []):
                print(temp.data)
            else:
                print(temp.data, end='->')

    def print_postorder(self):
        stack = []
        postorder = []
        stack.append(self.root)
        while(stack != []):
            temp = stack.pop()
            postorder.append(temp.data)
            if(temp.left != None):
                stack.append(temp.left)
            if(temp.right != None):
                stack.append(temp.right)
        while(postorder != []):
            if(len(postorder) > 1):
                print(postorder.pop(), end='->')
            else:
                print(postorder.pop())
