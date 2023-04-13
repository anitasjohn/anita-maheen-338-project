from myLib.datastructures.linear.LLQueue import Queue
from myLib.datastructures.nodes.SNode import SNode
import pytest

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