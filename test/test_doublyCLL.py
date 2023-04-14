import pytest
from myLib.datastructures.nodes.DNode import DNode
from myLib.datastructures.linear.doublyCLL import CircularDoublyLinkedList


def test_insert_head():
    cdll = CircularDoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    cdll.insert_head(node1)
    assert cdll.head == node1
    assert cdll.tail == node1
    cdll.insert_head(node2)
    assert cdll.head == node2
    assert cdll.head.next == node1
    assert cdll.tail.previous == node2
    assert cdll.tail.next == cdll.head

def test_insert_tail():
    cdll = CircularDoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    cdll.insert_tail(node1)
    assert cdll.head == node1
    assert cdll.tail == node1
    cdll.insert_tail(node2)
    assert cdll.tail == node2
    assert cdll.tail.previous == node1
    assert cdll.head.next == node2
    assert cdll.tail.next == cdll.head

def test_insert():
    cdll = CircularDoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    cdll.insert(node1, 0)
    assert cdll.head == node1
    assert cdll.tail == node1
    cdll.insert(node2, 1)
    cdll.insert(node3, 1)
    cdll.insert(node4, 3)
    assert cdll.head == node1
    assert cdll.tail == node4
    assert cdll.head.next == node2
    assert cdll.tail.previous == node3
    assert cdll.head.next.next == node3
    assert cdll.head.next.next.next == node4
    assert cdll.tail.next == cdll.head
    assert cdll.head.previous == cdll.tail

def test_DeleteTail():
    cdll = CircularDoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    cdll.insert_head(node1)
    cdll.insert_head(node2)
    cdll.insert_head(node3)
    assert cdll.DeleteTail() == node1.value
    assert cdll.tail == node2
    assert cdll.head.next == cdll.tail
    assert cdll.tail.previous == cdll.head
    assert cdll.tail.next == cdll.head
    assert cdll.head.previous == cdll.tail

def test_Delete():
    cdll = CircularDoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    cdll.insert_head(node1)
    cdll.insert_head(node2)
    cdll.insert_head(node3)
    cdll.insert_head


def test_empty_list():
    cll = CircularDoublyLinkedList()
    assert cll.length == 0
    assert cll.head is None
    assert cll.tail is None
    assert cll.DeleteHead() is None
    assert cll.DeleteTail() is None
    assert cll.Delete(DNode(10)) is None
def test_delete_node():
    c_dll = CircularDoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    c_dll.insert_head(node1)
    c_dll.insert_tail(node3)
    c_dll.insert(node2, 1)
    assert c_dll.Delete(node2) == 2
    assert c_dll.head is node1
    assert c_dll.tail is node3
    assert c_dll.head.next is node3
    assert c_dll.tail.previous is node1
    assert c_dll.length == 2


def test_insert_tail_empty_list():
     lst = CircularDoublyLinkedList()
     node = DNode(1)
     lst.insert_tail(node)
     assert lst.head == node
     assert lst.tail == node
     assert lst.head.prev == lst.tail
     assert lst.tail.next == lst.head
     assert lst.length == 1
