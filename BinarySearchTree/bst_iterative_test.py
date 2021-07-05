from BinarySearchTree.bst_iterative import *
from helper import *


def bst_iterative_test():
    print("Binary Search Tree Test")
    bst = BinarySearchTree()

    # empty BST
    bst.delete(0)
    bst.clear()
    print(bst.is_empty())
    print(bst.get_node(0))

    bst.insert(10)
    bst.insert(8)
    bst.insert(17)
    bst.insert(2)
    bst.insert(7)
    bst.insert(54)
    bst.insert(0)
    bst.print_inorder()
    bst.print_preorder()
    bst.print_postorder()
    bst.delete(0)
    print(bst.is_empty())
    bst.clear()
    print(bst.get_node(8))
