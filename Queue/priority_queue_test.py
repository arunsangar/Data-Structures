from Queue.priority_queue import *
from Utilities.helper import get_data


def priority_queue_test():
    print("Priority Queue Test")
    pq = PriorityQueue()

    # empty pq
    print(pq.dequeue())
    pq.clear()
    print(pq.front())
    print(pq.empty())
    print(pq.size())

    # multiple nodes
    data = get_data("TestFiles/numbers.txt")
    for d in data:
        pq.enqueue(d, d)
    pq.print()
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.front())
    print(pq.empty())
    print(pq.size())
    print(pq.get(15).data)
    pq.delete(15)
    pq.delete(12)
    pq.delete(20)
    pq.delete(3)
    pq.delete(1)
    pq.print()
    pq.clear()
    print(pq.empty())
