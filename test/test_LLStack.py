from myLib.datastructures.linear.LLStack import Stack
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode

import pytest
@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def stack_with_elements():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack


def test_push(empty_stack):
    empty_stack.push(1)
    assert empty_stack.peek() == 1


def test_pop(stack_with_elements):
    assert stack_with_elements.pop() == 3
    assert stack_with_elements.peek() == 2


def test_peek(empty_stack, stack_with_elements):
    assert empty_stack.peek() == None
    assert stack_with_elements.peek() == 3


def test_is_empty(empty_stack, stack_with_elements):
    assert empty_stack.is_empty() == True
    assert stack_with_elements.is_empty() == False


def test_override_methods(stack_with_elements):
    with pytest.raises(AttributeError):
        stack_with_elements.insert_tail(4)
    with pytest.raises(AttributeError):
        stack_with_elements.insert(5, 1)
    with pytest.raises(AttributeError):
        stack_with_elements.sortedInsert(6)