from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.linear.LLStack import Stack
from myLib.datastructures.nodes.SNode import SNode

import pytest


def test_push():
    stack = Stack()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    stack.push(node1)
    assert stack.peek() == 1
    assert stack.size() == 1
    stack.push(node2)
    assert stack.peek() == 2
    assert stack.size() == 2
    stack.push(node3)
    assert stack.peek() == 3
    assert stack.size() == 3

def test_pop():
    stack = Stack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    assert stack.pop().value == 3
    assert stack.size() == 2
    assert stack.pop().value == 2
    assert stack.size() == 1
    assert stack.pop().value == 1
    assert stack.size() == 0
    assert stack.pop() is None