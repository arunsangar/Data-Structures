from helper import TreeNode


class BSTRecursive:
    def __init__(self):
        self.root = None

    # wrapper function - insert_node
    def insert(self, x):
        self.insert_node(x, self.root)

    def insert_node(self, x, current):
        if(self.root == None):
            self.root = TreeNode(x)
        # left subtree
        elif(current.data > x):
            # if empty, add node
            if(current.left == None):
                current.left = TreeNode(x)
            # else recurse down left subtree
            else:
                self.insert_node(x, current.left)
        # right subtree
        elif(current.data < x):
            # if empty, add node
            if(current.right == None):
                current.right = TreeNode(x)
            # else recurse down right subtree
            else:
                self.insert_node(x, current.right)
        # duplicate node condition
        else:
            return

    # wrapper function - delete_node
    def delete(self, x):
        self.delete_node(x, self.root, None)

    def delete_node(self, x, current, previous):
        # empty BST
        if(current == None):
            return
        # left subtree
        if(current.data > x):
            self.delete_node(x, current.left, current)
        # right subtree
        elif(current.data < x):
            self.delete_node(x, current.right, current)
        # current nodes is set for deletion
        else:
            # node has at most one child
            if(current.left == None or current.right == None):
                child = None
                # choose child to replace current node
                if(current.left == None):
                    child = current.right
                else:
                    child = current.left
                # node is root
                if(previous == None):
                    self.root = child
                    return
                # replace node with child
                if(previous.left == current):
                    previous.left = child
                else:
                    previous.right = child
            # node has two children
            else:
                parent = None
                successor = current.right
                # find the successor node from the right subtree
                while(successor.left != None):
                    parent = successor
                    successor = successor.left
                # successor's parent is not root
                if(parent != None):
                    parent.left = successor.right
                # successor's parent is the root
                else:
                    current.right = successor.right
                current.data = successor.data

    def clear(self):
        temp = self.root
        while(temp != None):
            self.delete(temp.data)
            temp = self.root

    def top(self):
        if(self.root == None):
            return None
        return self.root.data

    # wrapper function - get_node
    def get(self, x):
        return self.get_node(x, self.root)

    def get_node(self, x, current):
        # empty BST or node not found
        if(current == None):
            return None
        # look in left subtree
        if(current.data > x):
            return self.get_node(x, current.left)
        # look in right subtree
        elif(current.data < x):
            return self.get_node(x, current.right)
        # node is found
        else:
            return current

    def is_empty(self):
        if(self.root == None):
            return True
        return False

    def print(self, order='inorder'):
        data = []
        # select order type
        if(order == 'inorder'):
            data = self.inorder(self.root)
        elif(order == 'preorder'):
            data = self.preorder(self.root)
        else:
            data = self.postorder(self.root)
        # print ordered list
        while(data != []):
            if(len(data) > 1):
                print(data.pop(0), end='->')
            else:
                print(data.pop(0))

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
