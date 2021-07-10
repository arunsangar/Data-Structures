from LinkedList.double_linked_list import *
from Utilities.helper import get_data


def double_linked_list_test():
    print("Double Linked List Test")
    dll = DoubleLinkedList()

    dll.clear()
    print(dll.head())
    print(dll.get(0))
    print(dll.empty())
    print(dll.size())
    dll.delete(0)
    dll.insert(1, 1)
    dll.insert(1, 0)
    dll.prepend(0)
    dll.append(2)
    dll.print()
    dll.clear()

    data = get_data("TestFiles/numbers.txt")
    for d in data:
        dll.insert(d)
    dll.print('backward')
    print(dll.head())
    print(dll.get(5))
    print(dll.empty())
    print(dll.size())
    dll.delete(5)
    dll.delete(7)
    dll.print()
    dll.clear()
