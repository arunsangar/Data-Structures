from LinkedList.linked_list import *
from numbers import *


def linked_list_test():
    print("Linked List Test")
    linkedlist = LinkedList()

    # empty list
    linkedlist.delete(2)
    linkedlist.get_node(2)
    print(linkedlist.get_size())
    linkedlist.print()

    linkedlist.insert(1, 0)
    linkedlist.print()
    linkedlist.delete(1)

    linkedlist.prepend(1)
    linkedlist.print()
    linkedlist.delete(1)

    linkedlist.append(1)
    linkedlist.print()
    linkedlist.delete(1)

    # 1 node
    linkedlist.insert(1, 0)
    linkedlist.delete(2)
    linkedlist.get_node(2)
    print(linkedlist.get_size())
    linkedlist.print()

    linkedlist.get_node(1)
    linkedlist.insert(2, 0)
    linkedlist.print()
    linkedlist.delete(2)

    linkedlist.prepend(2)
    linkedlist.print()
    linkedlist.delete(2)

    linkedlist.append(2)
    linkedlist.print()
    linkedlist.delete(2)

    linkedlist.delete(1)

    # multiple nodes
    linkedlist.insert(1, 0)
    linkedlist.append(2)
    linkedlist.insert(3, 2)
    linkedlist.prepend(0)
    linkedlist.append(4)

    print(linkedlist.get_size())
    linkedlist.get_node(5)
    linkedlist.get_node(3)
    linkedlist.print()

    linkedlist.delete(2)
    linkedlist.delete(2)
    linkedlist.delete(3)
    linkedlist.delete(4)
    linkedlist.delete(1)
    linkedlist.delete(0)
    linkedlist.delete(3)
    linkedlist.print()
