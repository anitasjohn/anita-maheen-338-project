from myLib.datastructures.linear.doublyCLL import CircularDoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode
import pytest



def test_circular_doubly_linked_list_init():
    c_dll = CircularDoublyLinkedList()
    assert c_dll.head is None
    assert c_dll.tail is None
    assert c_dll.length == 0