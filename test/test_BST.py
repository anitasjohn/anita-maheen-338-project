
from final338proj.myLib.datastructures.trees.BST import BST
from final338proj.myLib.datastructures.nodes.TNode import TNode
from queue import Queue
import pytest

@pytest.fixture
def bst():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    return bst
def test_insert(bst):
    bst.insert(2)
    assert bst.search(2).get_data() == 2



def test_insert_node(bst):
    node = TNode(9)
    bst.insert_node(node)
    assert bst.search(9).get_data() == 9


def test_delete_leaf(bst):
    bst.delete(4)
    assert bst.search(4) is None

def test_delete_node_with_one_child():
    # Create a binary search tree and insert some nodes
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # Delete a node with one child
    bst.delete(7)

    # Check that the node was deleted and the tree is still a valid BST
    assert bst.search(7) is None
    assert bst.search(6) is not None
    assert bst.search(8) is not None
    bst.print_in_order()  # Print the tree to visually inspect it


def test_delete_node_with_two_children(bst):
    bst.delete(7)
    assert bst.search(7) is None
    assert bst.search(6).get_data() == 6
    assert bst.search(8).get_data() == 8

def test_search(bst):
    assert bst.search(7).get_data() == 7
    assert bst.search(2) is None
def test_print_in_order(capsys, bst):
    bst.print_in_order()
    captured = capsys.readouterr()
    assert captured.out == "1 3 4 5 6 7 8\n"

def test_print_bf(capsys, bst):
    bst.print_bf()
    captured = capsys.readouterr()
    assert captured.out == "5 \n3 7 \n1 4 6 8 \n"



































'''def setUp(self):
    self.bst = BST()

def test_insert(self):
    self.bst.insert(10)
    self.bst.insert(5)        
    self.bst.insert(15)
    self.assertEqual(self.bst.print_in_order(), "5 10 15")
        
def test_insert_node(self):
    node1 = TNode(10)
    node2 = TNode(5)
    self.bst.insert_node(node1)
    self.bst.insert_node(node2)
    self.assertEqual(self.bst.search(10), node1)
    self.assertEqual(self.bst.search(5), node2)

def test_delete(self):
    self.bst.insert(10)
    self.bst.insert(5)
    self.bst.insert(15)
    self.bst.insert(7)
    self.bst.delete(5)
    self.assertEqual(self.bst.print_in_order(), "7 10 15")

def test_search(self):
    self.bst.insert(10)
    self.bst.insert(5)
    self.bst.insert(15)
    self.assertEqual(self.bst.search(10).get_data(), 10)
    self.assertEqual(self.bst.search(5).get_data(), 5)
    self.assertEqual(self.bst.search(15).get_data(), 15)
    self.assertEqual(self.bst.search(7), None)

def test_print_in_order(self):
    self.bst.insert(10)
    self.bst.insert(5)
    self.bst.insert(15)
    self.assertEqual(self.bst.print_in_order(), "5 10 15")

def test_print_bf(self):
    self.bst.insert(10)
    self.bst.insert(5)
    self.bst.insert(15)
    self.bst.insert(7)
    self.bst.insert(12)
    self.bst.insert(20)
    expected_output = "10 \n5 15 \n7 12 20 \n"
    self.assertEqual(self.bst.print_bf(), expected_output)

def test_get_successor(self):
    self.bst.insert(10)
    self.bst.insert(5)
    self.bst.insert(15)
    self.bst.insert(7)
    self.bst.insert(12)
    self.bst.insert(20)
    node = self.bst.search(10)
    self.assertEqual(self.bst.get_successor(node).get_data(), 12)
'''