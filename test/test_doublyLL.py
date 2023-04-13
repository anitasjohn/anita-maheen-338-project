from myLib.datastructures.linear.doublyLL import DoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode

import pytest

def test_insert_head():
    dll = DoublyLinkedList()
    node = DNode(5)
    dll.insert_head(node)
    assert dll.head.value == 5
    assert dll.tail.value == 5

def test_insert_tail():
    dll = DoublyLinkedList()
    node = DNode(5)
    dll.insert_tail(node)
    assert dll.head.value == 5
    assert dll.tail.value == 5

def test_insert():
    dll = DoublyLinkedList()
    node = DNode(5)
    node1 = DNode(10)
    node2 = DNode(15)
    dll.insert(node, 0)
    dll.insert(node1, 1)
    dll.insert(node2, 2)
    assert dll.head.value == 5
    assert dll.head.next.value == 10
    assert dll.head.next.next.value == 15
    assert dll.tail.value == 15
def test_DeleteHead():
    dll = DoublyLinkedList()
    node = DNode(5)
    node1 = DNode(10)
    node2 = DNode(15)
    dll.insert_tail(node)
    dll.insert_tail(node1)
    dll.insert_tail(node2)
    dll.DeleteHead()
    assert dll.head.value == 10

def test_DeleteTail():
    dll = DoublyLinkedList()
    node = DNode(5)
    node1 = DNode(10)
    node2 = DNode(15)
    dll.insert_tail(node)
    dll.insert_tail(node1)
    dll.insert_tail(node2)
    dll.DeleteTail()
    assert dll.tail.value == 10

def test_Delete():
    dll = DoublyLinkedList()

    node =  DNode(5)
    node1 = DNode(10)
    node2 = DNode(15)
    dll.insert_tail(node)
    dll.insert_tail(node1)
    dll.insert_tail(node2)
    dll.Delete(dll.head.next)
    assert dll.head.next.value == 15
    assert dll.tail.value == 15

