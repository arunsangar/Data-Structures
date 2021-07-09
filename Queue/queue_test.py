from Queue.queue import *
from Utilities.helper import get_data


def queue_test():
    print("Queue Test")
    queue = Queue()

    # empty queue
    print(queue.dequeue())
    queue.clear()
    print(queue.front())
    print(queue.empty())
    print(queue.size())

    # multiple nodes
    data = get_data("TestFiles/numbers.txt")
    for d in data:
        queue.enqueue(d)
    queue.print()
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.front())
    print(queue.empty())
    print(queue.size())
    print(queue.get(15).data)
    queue.delete(15)
    queue.delete(12)
    queue.delete(20)
    queue.delete(3)
    queue.delete(1)
    queue.print()
    queue.clear()
    print(queue.empty())
