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
    print(stack.size())

    # multiple nodes
    data = get_data("Numbers/numbers.txt")
    for d in data:
        stack.push(d)
    stack.print()
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.is_empty())
    print(stack.size())
    stack.clear()
    print(stack.is_empty())
