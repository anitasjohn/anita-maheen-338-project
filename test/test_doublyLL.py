from myLib.datastructures.linear.doublyLL import DoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode

import pytest

@pytest.fixture
def empty_dlist():
    return DoublyLinkedList()

@pytest.fixture
def dlist_with_nodes():
    dlist = DoublyLinkedList()
    dlist.insert_head(DNode(1))
    dlist.insert_tail(DNode(2))
    dlist.insert(DNode(3), 1)
    return dlist

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



def test_insert_head(empty_dlist):
    node = DNode(1)
    empty_dlist.insert_head(node)
    assert empty_dlist.head == node
    assert empty_dlist.tail == node
def test_insert_tail(empty_dlist):
    node = DNode(1)
    empty_dlist.insert_tail(node)
    assert empty_dlist.head == node
    assert empty_dlist.tail == node

def test_insert_position_negative():
    linked_list = DoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    with pytest.raises(Exception):
        linked_list.insert(node1, -1)
    linked_list.insert_head(node1)
    with pytest.raises(Exception):
        linked_list.insert(node2, -1)
def test_delete_tail_empty_list():
    doubly_ll = DoublyLinkedList()
    assert doubly_ll.DeleteTail() == None
    assert doubly_ll.head == None
    assert doubly_ll.tail == None

def test_delete_head_empty_list():
    doubly_ll = DoublyLinkedList()
    doubly_ll.DeleteHead()
    assert doubly_ll.head == None
    assert doubly_ll.tail == None
def test_delete_node_not_in_list():
    dll = DoublyLinkedList()
    
    node = DNode(1)
    assert dll.Delete(node) == None

def test_insert_position_greater_than_length():
    dll = DoublyLinkedList()
    dll.insert(DNode(1), 10)
    assert dll.head.value == 1
    assert dll.tail.value == 1

def test_delete_tail_empty_list():
    dll = DoublyLinkedList()
    assert dll.DeleteTail() == None

def test_delete_middle_node():
    dll = DoublyLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    dll.insert_head(node1)
    dll.insert_tail(node2)
    dll.insert_tail(node3)
    assert dll.Delete(node2) == 2
    assert dll.head.value == 1
    assert dll.tail.value == 3
    assert dll.head.next.value == 3
    assert dll.tail.previous.value == 1



