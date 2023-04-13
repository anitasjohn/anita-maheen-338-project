from myLib.datastructures.linear.LLStack import Stack
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
import pytest

def test_push():
    stack = Stack()
    node = SNode(1)
    stack.push(node)
    assert stack.peek() == 1
def test_pop():
    stack = Stack()
    node = SNode(1)
    node1 = SNode(2)

    stack.push(node)
    stack.push(node1)
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.peek() is None
    assert stack.is_empty() is True

def test_peek():
    stack = Stack()
    node = SNode(1)
    stack.push(node)
    assert stack.peek() == 1

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False

