import pytest
from myLib.datastructures.linear.LLStack import Stack
from myLib.datastructures.nodes.SNode import SNode


@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def filled_stack():
    stack = Stack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    return stack

def test_push(empty_stack):
    empty_stack.push(SNode(1))
    assert empty_stack.peek() == 1
    assert empty_stack.length == 1

def test_pop(filled_stack):
    assert filled_stack.pop() == 3
    assert filled_stack.pop() == 2
    assert filled_stack.pop() == 1
    assert filled_stack.is_empty()

def test_peek(filled_stack):
    assert filled_stack.peek() == 3
    assert filled_stack.length == 3

def test_is_empty(empty_stack):
    assert empty_stack.is_empty()
    empty_stack.push(SNode(1))
    assert not empty_stack.is_empty()
    empty_stack.pop()
    assert empty_stack.is_empty()



