import pytest

from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode


def test_insert_head():
    linked_list = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)

    # Test inserting into an empty list
    linked_list.insert_head(node1)
    assert linked_list.head == node1
    assert linked_list.tail == node1
    assert linked_list.length == 1

    # Test inserting into a non-empty list
    linked_list.insert_head(node2)
    assert linked_list.head == node1
    assert linked_list.head.next == node2
    assert linked_list.tail == node1
    assert linked_list.length == 2