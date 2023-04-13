from myLib.datastructures.linear.LLQueue import Queue
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
import pytest

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def queue_with_items():
    q = Queue()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    q.enqueue(SNode(3))
    return q

def test_enqueue():
    q = Queue()
    assert q.is_empty()
    node1 = SNode(1)
    node2 = SNode(2)
    q.enqueue(node1)
    assert not q.is_empty()
    assert q.peek() == node1.value
    q.enqueue(node2)
    assert q.peek() == node1.value
def test_dequeue():
    q = Queue()
    node1 = SNode(1)
    node2 = SNode(2)
    q.enqueue(node1)
    q.enqueue(node2)
    assert q.dequeue() == node1.value
    assert q.peek() == node2.value
    assert q.dequeue() == node2.value
    assert q.is_empty()
def test_peek():
    q = Queue()
    assert q.peek() is None
    node1 = SNode(1)
    q.enqueue(node1)
    assert q.peek() == node1.value

def test_sorted_insert():
    q = Queue()
    node1 = SNode(1)
    q.SortedInsert(node1) # should have no effect
    assert q.is_empty()


def test_delete_head():
    q = Queue()
    node1 = SNode(1)
    q.enqueue(node1)
    q.DeleteHead() # should have no effect
    assert q.peek() == node1.value
def test_delete_tail():
    q = Queue()
    node1 = SNode(1)
    q.enqueue(node1)
    q.DeleteTail() # should have no effect
    assert q.peek() == node1.value

def test_is_empty(empty_queue):
    assert empty_queue.is_empty() == True

def test_dequeue(empty_queue):
    assert empty_queue.dequeue() == None



def test_peek(empty_queue):
    assert empty_queue.peek() == None

def test_delete_head(empty_queue):
    assert empty_queue.DeleteHead() == None

def test_delete_tail(empty_queue):
    assert empty_queue.DeleteTail() == None

def test_enqueue_and_peek(queue_with_items):
    q = queue_with_items
    node = SNode(4)
    q.enqueue(node)
    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 2
    q.dequeue()
    assert q.peek() == 3
    q.dequeue()
    assert q.peek() == 4
    q.dequeue()
    assert q.peek() is None
def test_enqueue_and_dequeue(queue_with_items):
    q = queue_with_items
    node = SNode(4)
    q.enqueue(node)
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.peek() == 2
    assert q.dequeue() == 2
    assert q.peek() == 3
    assert q.dequeue() == 3
    assert q.peek() == 4
    assert q.dequeue() == 4
    assert q.is_empty()
def test_enqueue_empty_node():
    q = Queue()
    node = SNode(None)
    q.enqueue(node)
    assert q.peek() is None
    assert not q.is_empty()

def test_dequeue_empty_queue():
    q = Queue()
    assert q.dequeue() is None

def test_peek_empty_queue():
    q = Queue()
    assert q.peek() is None

def test_delete_head(empty_queue):
    assert empty_queue.DeleteHead() is None

def test_delete_tail(empty_queue):
    assert empty_queue.DeleteTail() is None

def test_delete(empty_queue):
    assert empty_queue.Delete(SNode(1)) is None
def test_enqueue_and_peek():
    q = Queue()
    assert q.is_empty()
    node1 = SNode(1)
    node2 = SNode(2)
    q.enqueue(node1)
    assert not q.is_empty()
    assert q.peek() == node1.value
    q.enqueue(node2)
    assert q.peek() == node1.value
def test_enqueue_empty_node():
    q = Queue()
    node = SNode(None)
    q.enqueue(node)
    assert q.peek() is None
    assert not q.is_empty()

def test_override_methods():
    q = Queue()
    assert q.SortedInsert(None) == None
    assert q.isSorted() == None
    assert q.Search(None) == None
    assert q.DeleteHead() == None
    assert q.DeleteTail() == None
    assert q.Delete(None) == None
def test_is_empties():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    assert q.is_empty() == False


def test_peek_empty_queue():
    q = Queue()
    assert q.peek() == None
def test_is_empty_false():
    q = Queue()
    q.enqueue(1)
    assert q.is_empty() == False


