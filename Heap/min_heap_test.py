from Heap.min_heap import *
from helper import *


def min_heap_test():
    print("Min Heap Test")
    heap = MinHeap()

    print(heap.size())
    print(heap.height())
    heap.insert(31)
    heap.insert(10)
    heap.insert(17)
    heap.insert(24)
    heap.insert(14)
    heap.insert(7)
    print(heap.size())
    print(heap.height())
    heap.print('inorder')
    heap.print('preorder')
    heap.print('postorder')
    heap.delete(10)
    heap.delete(31)
    heap.delete(54)
    print(heap.size())
    print(heap.height())
    heap.print('inorder')
    heap.delete(7)
    heap.delete(1)
    print(heap.size())
    print(heap.height())
    heap.print('inorder')
