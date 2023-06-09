import pytest

from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
@pytest.fixture
def lst():
    return SinglyLinkedList()
def test_insert_head():
    sll = SinglyLinkedList()
    sll.insert_head(SNode(1))
    assert sll.head.value == 1
    assert sll.tail.value == 1
    sll.insert_head(SNode(2))
    assert sll.head.value == 2
    assert sll.tail.value == 1

def test_insert_tail():
    ll = SinglyLinkedList()
    assert ll.length == 0
    node1 = SNode(1)
    ll.insert_tail(node1)
    assert ll.length == 1
    assert ll.head == node1
    assert ll.tail == node1
    node2 = SNode(2)
    ll.insert_tail(node2)
    assert ll.length == 2
    assert ll.tail == node2
    assert ll.head.next == node2
def test_insert():
    ll = SinglyLinkedList()
    assert ll.length == 0

    node1 = SNode(1)
    ll.insert(node1, 0)
    assert ll.length == 1

    node2 = SNode(2)
    ll.insert(node2, 1)

    assert ll.length == 2

    node3 = SNode(3)
    ll.insert(node3, 1)
    assert ll.length == 3
def test_sorted_insert():
    sll = SinglyLinkedList()
    sll.SortedInsert(SNode(3))
    assert sll.head.value == 3
    assert sll.tail.value == 3
    sll.SortedInsert(SNode(1))
    assert sll.head.value == 1
    assert sll.tail.value == 3
    sll.SortedInsert(SNode(2))
    assert sll.head.value == 1
    assert sll.tail.value == 3
def test_is_sorted():
    sll = SinglyLinkedList()
    assert sll.isSorted() is True
    sll.insert_tail(SNode(1))
    assert sll.isSorted() is True
    sll.insert_tail(SNode(2))
    assert sll.isSorted() is True
    sll.insert_tail(SNode(0))
    assert sll.isSorted() is False
def test_Search():
    sll = SinglyLinkedList()
    sll.insert_tail(SNode(1))
    sll.insert_tail(SNode(2))
    sll.insert_tail(SNode(3))
    assert sll.Search(1).value == 1
    assert sll.Search(4) is None
def test_DeleteHead():
    sll = SinglyLinkedList()
    sll.insert_tail(SNode(1))
    sll.DeleteHead()
    assert sll.head is None
    assert sll.tail is None
    assert sll.length == 0
    sll.insert_tail(SNode(1))
    sll.insert_tail(SNode(2))
    sll.DeleteHead()
    assert sll.head.value == 2
def test_DeleteTail():
    sll = SinglyLinkedList()
    sll.DeleteTail()
    assert sll.head is None
    assert sll.tail is None
    assert sll.length == 0
    sll.insert_tail(SNode(1))
    sll.insert_tail(SNode(2))
    sll.insert_tail(SNode(3))
    sll.DeleteTail()
    assert sll.tail.value == 2
    sll.DeleteTail()
    assert sll.tail.value == 1
    sll.DeleteTail()
    assert sll.head is None
    assert sll.tail is None
    assert sll.length == 0

def test_Delete():
    sll = SinglyLinkedList()
    sll.insert_tail(SNode(1))
    sll.insert_tail(SNode(2))
    sll.insert_tail(SNode(3))
    assert sll.Delete(sll.Search(2)) == 2
    assert sll.length == 2
    assert sll.Search(2) is None
    assert sll.Delete(SNode(4)) is None

def test_is_sorted():
    sll = SinglyLinkedList()
    assert sll.isSorted() == True
    
    sll.insert_head(SNode(3))
    assert sll.isSorted() == True
    
    sll.insert_tail(SNode(5))
    assert sll.isSorted() == True
    
    sll.insert_tail(SNode(4))
    assert sll.isSorted() == False
    
    sll.Sort()
    assert sll.isSorted() == True
def test_search():
    sll = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    sll.insert_head(node1)
    sll.insert_tail(node2)
    sll.insert_tail(node3)
    assert sll.Search(2) == node2
    assert sll.Search(4) == None
def test_delete_head_from_empty_list():
    sll = SinglyLinkedList()
    sll.DeleteHead()
    assert sll.length == 0
def test_DeleteTail():
    sll = SinglyLinkedList()
    sll.DeleteTail()
    assert sll.head is None
    assert sll.tail is None
    assert sll.length == 0
    sll.insert_tail(SNode(1))
    sll.insert_tail(SNode(2))
    sll.insert_tail(SNode(3))
    sll.DeleteTail()
    assert sll.tail.value == 2
    sll.DeleteTail()
    assert sll.tail.value == 1
def test_delete(lst):
    lst.insert_tail(SNode(1))
    node2 = SNode(2)
    lst.insert_tail(node2)
    lst.insert_tail(SNode(3))
    lst.Delete(node2)
    assert lst.head.value == 1
    assert lst.tail.value == 3
    assert lst.length == 2
def test_sort(lst):
    lst.insert_tail(SNode(3))
    lst.insert_tail(SNode(2))
    lst.insert_tail(SNode(1))
    lst.Sort()
    assert lst.head.value == 1
    assert lst.tail.value == 3
    assert lst.length == 3
def test_clear(lst):
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.Clear()
    assert lst.head is None
    assert lst.tail is None
    assert lst.length == 0

def test_print_empty(lst, capsys):
    lst.Print()
    captured = capsys.readouterr()
    assert captured.out == "List is empty\n"

def test_print_non_empty(lst, capsys):
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.Print()
    captured = capsys.readouterr()
    assert captured.out == "1 -> 2 -> None\n"

    llist = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    llist.insert_head(node1)
    llist.insert_head(node2)
    assert llist.head == node2
    assert llist.tail == node1
def test_SortedInsert_unsorted_list():
    llist = SinglyLinkedList()
    node1 = SNode(2)
    node2 = SNode(1)
    llist.SortedInsert(node1)
    llist.SortedInsert(node2)
    assert llist.head == node2
    assert llist.tail == node1

def test_Search_value_not_in_list():
    llist = SinglyLinkedList()
    node = SNode(1)
    llist.insert_head(node)
    assert llist.Search(2) is None

def test_SortedInsert_unsorted_list():
    llist = SinglyLinkedList()
    node1 = SNode(2)
    node2 = SNode(1)
    llist.SortedInsert(node1)
    llist.SortedInsert(node2)
    assert llist.head == node2
    assert llist.tail == node1

def test_insert_position_end_of_list():
    llist = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    llist.insert_tail(node1)
    llist.insert_tail(node2)
    llist.insert(node3, 2)
    assert llist.tail == node3
def test_insert_negative_position():
    llist = SinglyLinkedList()
    node = SNode(1)
    with pytest.raises(ValueError):
        llist.insert(node, -1)

def test_insert_position_zero():
    llist = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    llist.insert(node1, 0)
    llist.insert(node2, 0)
    assert llist.head == node2
    assert llist.tail == node1
