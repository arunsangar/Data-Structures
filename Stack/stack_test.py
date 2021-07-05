from Stack.stack import *
from helper import *


def stack_test():
    print("Stack Test")
    stack = Stack()

    # empty stack
    print(stack.pop())
    stack.clear()
    print(stack.top())
    print(stack.is_empty())
    print(stack.get_size())

    # multiple nodes
    data = get_data("Data-Structures/numbers.txt")
    for d in data:
        stack.push(d)
    stack.print()
    print(stack.pop())
    print(stack.pop().data)
    print(stack.top())
    print(stack.is_empty())
    print(stack.get_size())
    stack.clear()
    print(stack.is_empty())
