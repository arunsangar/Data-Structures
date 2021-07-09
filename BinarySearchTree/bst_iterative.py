from Utilities.nodes import TreeNode
from Utilities.make_list import inorder
from Utilities.make_list import preorder
from Utilities.make_list import postorder
from Utilities.helper import print_list


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
    def empty(self):
        if(self.__root == None):
            return True
        return False

    # print BST inorder, preorder or postorder
    def print(self, order='inorder'):
        data = []
        # select order type
        if(order == 'inorder'):
            print_list(inorder(self.__root))
        elif(order == 'preorder'):
            print_list(preorder(self.__root))
        else:
            print_list(postorder(self.__root))
