from BinarySearchTree.bst_recursive import *


def bst_recursive_test():
    print("Binary Search Tree Test (recursive)")
    bst = BSTRecursive()

    # empty BST
    bst.delete(0)
    bst.clear()
    print(bst.empty())
    print(bst.get(0))

    bst.insert(10)
    bst.insert(8)
    bst.insert(17)
    bst.insert(2)
    bst.insert(7)
    bst.insert(54)
    bst.insert(0)
    bst.print('inorder')
    bst.print('preorder')
    bst.print('postorder')
    bst.delete(0)
    print(bst.empty())
    bst.clear()
    print(bst.get(8))
