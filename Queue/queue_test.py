from Queue.queue import *
from Utilities.helper import get_data


def queue_test():
    print("Queue Test")
    queue = Queue()

    # empty queue
    print(queue.pop())
    queue.clear()
    print(queue.top())
    print(queue.empty())
    print(queue.size())

    # multiple nodes
    data = get_data("TestFiles/numbers.txt")
    for d in data:
        queue.push(d)
    queue.print()
    print(queue.pop())
    print(queue.pop())
    print(queue.top())
    print(queue.empty())
    print(queue.size())
    queue.clear()
    print(queue.empty())
