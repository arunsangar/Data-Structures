from LinkedList.circular_linked_list import *


def circular_linked_list_test():
    print("Circular Linked List Test")
    cll = CircularLinkedList()

    # empty list
    cll.delete(2)
    print(cll.get(2))
    print(cll.size())
    cll.print()
    cll.insert(1, 0)
    cll.print()
    cll.delete(1)

    # 1 node
    cll.insert(1, 0)
    cll.delete(2)
    print(cll.get(2))
    print(cll.size())
    cll.print()
    print(cll.get(1))
    cll.insert(2, 0)
    cll.print()
    cll.delete(2)
    cll.delete(1)

    # multiple nodes
    cll.insert(1, 0)
    cll.append(2)
    cll.insert(3, 2)
    cll.prepend(0)
    cll.append(4)
    cll.insert(6, 2)
    cll.insert(8, 2)
    cll.prepend(5)
    cll.prepend(10)

    print(cll.head())
    print(cll.size())
    print(cll.get(15))
    print(cll.get(3))
    cll.print()
    cll.print('backward')

    cll.delete(2)
    cll.delete(2)
    cll.delete(3)
    cll.delete(4)
    cll.delete(1)
    cll.delete(0)
    cll.delete(3)
    cll.print()
    cll.clear()
    cll.print()
