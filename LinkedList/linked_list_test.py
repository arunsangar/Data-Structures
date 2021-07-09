from LinkedList.linked_list import *


def linked_list_test():
    print("Linked List Test")
    linkedlist = LinkedList()

    # empty list
    linkedlist.delete(2)
    print(linkedlist.get(2))
    print(linkedlist.size())
    linkedlist.print()
    linkedlist.insert(1, 0)
    linkedlist.print()
    linkedlist.delete(1)

    # 1 node
    linkedlist.insert(1, 0)
    linkedlist.delete(2)
    print(linkedlist.get(2))
    print(linkedlist.size())
    linkedlist.print()
    print(linkedlist.get(1))
    linkedlist.insert(2, 0)
    linkedlist.print()
    linkedlist.delete(2)
    linkedlist.delete(1)

    # multiple nodes
    linkedlist.insert(1, 0)
    linkedlist.append(2)
    linkedlist.insert(3, 2)
    linkedlist.prepend(0)
    linkedlist.append(4)
    linkedlist.insert(6, 2)
    linkedlist.insert(8, 2)
    linkedlist.prepend(5)
    linkedlist.prepend(10)

    print(linkedlist.head())
    print(linkedlist.size())
    print(linkedlist.get(15))
    print(linkedlist.get(3))
    linkedlist.print()
    linkedlist.print('backward')

    linkedlist.delete(2)
    linkedlist.delete(2)
    linkedlist.delete(3)
    linkedlist.delete(4)
    linkedlist.delete(1)
    linkedlist.delete(0)
    linkedlist.delete(3)
    linkedlist.print()
    linkedlist.clear()
    linkedlist.print()
