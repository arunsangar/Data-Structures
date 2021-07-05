from Queue.queue import *
from helper import *


def queue_test():
    print("Queue Test")
    queue = Queue()

    # empty queue
    print(queue.pop())
    queue.clear()
    print(queue.top())
    print(queue.is_empty())
    print(queue.get_size())

    # multiple nodes
    data = get_data("Data-Structures/numbers.txt")
    for d in data:
        queue.push(d)
    queue.print()
    print(queue.pop())
    print(queue.pop().data)
    print(queue.top())
    print(queue.is_empty())
    print(queue.get_size())
    queue.clear()
    print(queue.is_empty())
