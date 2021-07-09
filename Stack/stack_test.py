from Stack.stack import *
from Utilities.helper import get_data


def stack_test():
    print("Stack Test")
    stack = Stack()

    # empty stack
    print(stack.pop())
    stack.clear()
    print(stack.top())
    print(stack.empty())
    print(stack.size())

    # multiple nodes
    data = get_data("TestFiles/numbers.txt")
    for d in data:
        stack.push(d)
    stack.print()
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.empty())
    print(stack.size())
    stack.clear()
    print(stack.empty())
