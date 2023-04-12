from myLib.datastructures.linear.singlyCLL import CircularSinglyLinkedList
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode


def test_circular_singly_linked_list_init():
    node = SNode(5)
    c_list = CircularSinglyLinkedList(node)
    assert c_list.head == node
    assert c_list.tail == node
    assert c_list.head.next == node
    assert c_list.length == 1
def test_circular_singly_linked_list_insert_tail():
    node1 = SNode(5)
    node2 = SNode(6)
    node3 = SNode(7)
    c_list = CircularSinglyLinkedList(node1)
    c_list.insert_tail(node2)
    c_list.insert_tail(node3)
    assert c_list.head == node1
    assert c_list.head.next == node2
    assert c_list.tail == node3
    assert c_list.tail.next == node1
    assert c_list.length == 3
def test_circular_singly_linked_list_delete_head():
    node1 = SNode(5)
    node2 = SNode(6)
    node3 = SNode(7)
    c_list = CircularSinglyLinkedList(node1)
    c_list.insert_tail(node2)
    c_list.insert_tail(node3)
    assert c_list.DeleteHead() == 5
    assert c_list.head == node2
    assert c_list.head.next == node3
    assert c_list.tail == node3
    assert c_list.tail.next == node2
    assert c_list.length == 2
def test_circular_singly_linked_list_delete_tail():
    node1 = SNode(5)
    node2 = SNode(6)
    node3 = SNode(7)
    c_list = CircularSinglyLinkedList(node1)
    c_list.insert_tail(node2)
    c_list.insert_tail(node3)
    assert c_list.DeleteTail() == 7
    assert c_list.head == node1
    assert c_list.head.next == node2
    assert c_list.tail == node2
    assert c_list.tail.next == node1
    assert c_list.length == 2
def test_print_empty_list(capsys):
    llist = CircularSinglyLinkedList()
    llist.Print()
    captured = capsys.readouterr()
    assert captured.out == "List length: 0\nList content:\n"
    
def test_print_list_with_one_node(capsys):
    node = SNode(42)
    llist = CircularSinglyLinkedList(node)
    llist.Print()
    captured = capsys.readouterr()
    assert captured.out == "List length: 1\nList content:\n42\n"
    
def test_print_list_with_multiple_nodes(capsys):
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    llist = CircularSinglyLinkedList(node1)
    llist.insert_tail(node2)
    llist.insert_tail(node3)
    llist.Print()
    captured = capsys.readouterr()
    assert captured.out == "List length: 3\nList content:\n1\n2\n3\n"

def test_insert_tails():
    # Create an empty list
    cll = CircularSinglyLinkedList()
    
    # Insert a node at the tail
    cll.insert_tail(SNode(1))
    
    # Check that the head, tail, and length are correct
    assert cll.head.value == 1
    assert cll.tail.value == 1
    assert cll.length == 1
    
    # Insert another node at the tail
    cll.insert_tail(SNode(2))
    
    # Check that the head, tail, and length are correct
    assert cll.head.value == 1
    assert cll.tail.value == 2
    assert cll.length == 2


def test_DeleteHead():
    # Create a list with some nodes
    cll = CircularSinglyLinkedList(SNode(1))
    cll.insert_tail(SNode(2))
    cll.insert_tail(SNode(3))
    
    # Delete the head
    assert cll.DeleteHead() == 1
    
    # Check that the head, tail, and length are correct
    assert cll.head.value == 2
    assert cll.tail.value == 3
    assert cll.length == 2
    
    # Delete the head again
    assert cll.DeleteHead() == 2
    
    # Check that the head, tail, and length are correct
    assert cll.head.value == 3
    assert cll.tail.value == 3
    assert cll.length == 1
    
    # Delete the only remaining node
    assert cll.DeleteHead() == 3
    
    # Check that the list is now empty
    assert cll.head == None
    assert cll.tail == None
    assert cll.length == 0
def test_empty_list_creation():
    lst = CircularSinglyLinkedList()
    assert lst.head == None
    assert lst.tail == None
    assert lst.length == 0
def test_insert_head_nonempty_list():
    lst = CircularSinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    lst.insert_head(node1)
    lst.insert_head(node2)
    lst.insert_head(node3)
    assert lst.head == node3
    assert lst.tail == node1
    assert lst.length == 3
# test insert_tail on empty list
def test_insert_tail_empty_list():
    lst = CircularSinglyLinkedList()
    node = SNode(1)
    lst.insert_tail(node)
    assert lst.head == node
    assert lst.tail == node
    assert lst.length == 1

# test insert_tail on non-empty list
def test_insert_tail_nonempty_list():
    lst = CircularSinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    lst.insert_tail(node1)
    lst.insert_tail(node2)
    lst.insert_tail(node3)
    assert lst.head == node1
    assert lst.tail == node3
    assert lst.length == 3
# test DeleteHead on empty list
def test_DeleteHead_empty_list():
    lst = CircularSinglyLinkedList()
    assert lst.DeleteHead() == None
    assert lst.head == None
    assert lst.tail == None
    assert lst.length == 0

# test DeleteHead on list with one node
def test_DeleteHead_one_node_list():
    lst = CircularSinglyLinkedList(SNode(1))
    assert lst.DeleteHead() == 1
    assert lst.head == None
    assert lst.tail == None
    assert lst.length == 0
# test DeleteHead on list with multiple nodes
def test_DeleteHead_multiple_node_list():
    lst = CircularSinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    lst.insert_head(node1)
    lst.insert_head(node2)
    lst.insert_head(node3)
    assert lst.DeleteHead() == 3
    assert lst.head == node2
    assert lst.tail == node1
    assert lst.length == 2

# test DeleteTail on empty list
def test_DeleteTail_empty_list():
    lst = CircularSinglyLinkedList()
    assert lst.DeleteTail() == None
    assert lst.head == None
    assert lst.tail == None
    assert lst.length == 0
# test DeleteTail on list with one node
def test_DeleteTail_one_node_list():
    lst = CircularSinglyLinkedList(SNode(1))
    assert lst.DeleteTail() == 1
    assert lst.head == None
    assert lst.tail == None
    assert lst.length == 0

