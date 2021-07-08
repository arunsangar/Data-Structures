from Heap.max_heap import *
from helper import *


def max_heap_test():
    print("Max Heap Test")
    heap = MaxHeap()

    print(heap.size())
    print(heap.height())
    heap.insert(1)
    heap.insert(10)
    heap.insert(17)
    heap.insert(20)
    heap.insert(3)
    heap.insert(7)
    print(heap.size())
    print(heap.height())
    heap.print('inorder')
    heap.print('preorder')
    heap.print('postorder')
    heap.delete(10)
    heap.delete(3)
    heap.delete(54)
    print(heap.size())
    print(heap.height())
    heap.print('inorder')
    heap.delete(7)
    heap.delete(1)
    print(heap.size())
    print(heap.height())
    heap.print('inorder')
