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

def test_push_multiple_nodes():
    stack = Stack()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    stack.push(node1)
    stack.push(node2)
    stack.push(node3)
    assert stack.peek() == 3
def test_pop_empty_stack():
    stack = Stack()
    assert stack.pop() == None

def test_pop_single_node_stack():
    stack = Stack()
    node = SNode(1)
    stack.push(node)
    assert stack.pop() == 1
    assert stack.peek() == None
def test_pop_multiple_nodes():
    stack = Stack()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    stack.push(node1)
    stack.push(node2)
    stack.push(node3)
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.peek() == None

def test_peek_empty_stack():
    stack = Stack()
    assert stack.peek() == None
def test_peek_single_node_stack():
    stack = Stack()
    node = SNode(1)
    stack.push(node)
    assert stack.peek() == 1

def test_is_empty_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

def test_is_empty_non_empty_stack():
    stack = Stack()
    node = SNode(1)
    stack.push(node)
    assert stack.is_empty() == False
def test_push_empty_stack():
    stack = Stack()
    node = SNode(1)
    stack.push(node)
    assert stack.peek() == 1


def test_peek_empty_stack():
    stack = Stack()
    assert stack.peek() is None

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() is True
    node = SNode(1)
    stack.push(node)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True

def test_pop_until_empty():
    stack = Stack()
    for i in range(10):
        node = SNode(i)
        stack.push(node)
    for i in reversed(range(10)):
        assert stack.pop() == i
    assert stack.pop() is None
