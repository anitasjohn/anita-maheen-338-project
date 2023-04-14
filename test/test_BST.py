
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
@pytest.fixture
def bstTree():
    return BST()

@pytest.fixture
def empty_bst():
    return BST()

@pytest.fixture
def bst_with_one_node():
    node = TNode(5)
    bst = BST(node)
    return bst

@pytest.fixture
def bst_with_two_nodes():
    node1 = TNode(5)
    node2 = TNode(3)
    bst = BST(node1)
    bst.insert_node(node2)
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

def test_searchs(bst):
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

def test_search(bst):
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(9)

    print(bst.search(5).get_data()) # expected output: 5
    print(bst.search(3).get_data()) # expected output: 3
    print(bst.search(7).get_data()) # expected output: 7
    print(bst.search(1).get_data()) # expected output: 1
    print(bst.search(9).get_data()) # expected output: 9

    assert bst.search(5).get_data() == 5
    assert bst.search(3).get_data() == 3
    assert bst.search(7).get_data() == 7
    assert bst.search(1).get_data() == 1
    assert bst.search(9).get_data() == 9

def test_print_in_order(capsys):
    bst = BST(TNode(5))
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(9)
    bst.print_in_order()
    captured = capsys.readouterr()
    assert captured.out == "1 3 5 7 9\n"

def test_print_bf(capsys):
    bst = BST(TNode(5))
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(9)
    bst.print_bf()
    captured = capsys.readouterr()
    assert captured.out == "5 \n3 7 \n1 9 \n"

def test_empty_tree():
    bst = BST()
    assert bst.get_root() is None
    assert bst.search(5) is None
    bst.print_in_order() # should return nothing
    bst.print_bf() # should return nothing
    bst.delete(5) # should return "Value not found in the tree"
def test_single_node_tree():
    bst = BST(TNode(5))
    assert bst.get_root().get_data() == 5
    assert bst.search(5).get_data() == 5
    bst.print_in_order() # should return 5
    bst.print_bf() # should return 5
    bst.delete(5)
    assert bst.get_root() is None
    assert bst.search(5) is None
    bst.print_in_order() # should return nothing
    bst.print_bf() # should return nothing
    bst.delete(5) # should return "Value not found in the tree"

def test_empty_bst(empty_bst):
    assert empty_bst.get_root() == None
    assert empty_bst.search(1) == None
    empty_bst.delete(1)  # nothing should happen
    empty_bst.print_in_order()  # nothing should be printed
    empty_bst.print_bf()  # nothing should be printed

def test_bst_with_one_node(bst_with_one_node):
    assert bst_with_one_node.get_root().get_data() == 5
    assert bst_with_one_node.search(5).get_data() == 5
    bst_with_one_node.delete(5)
    assert bst_with_one_node.get_root() == None
    bst_with_one_node.print_in_order()  # nothing should be printed
    bst_with_one_node.print_bf()  # nothing should be printed

def test_bst_with_two_nodes(bst_with_two_nodes):
    assert bst_with_two_nodes.get_root().get_data() == 5
    assert bst_with_two_nodes.search(5).get_data() == 5
    assert bst_with_two_nodes.search(3).get_data() == 3
    bst_with_two_nodes.delete(5)
    assert bst_with_two_nodes.get_root().get_data() == 3
    bst_with_two_nodes.print_in_order()  # should print "3"
    bst_with_two_nodes.print_bf()  # should print "3"


def test_search_nonexistent_value(bstTree):
    bstTree.insert(5)
    assert bstTree.search(7) is None

def test_delete_root_node(bstTree):
    bstTree.insert(5)
    bstTree.delete(5)
    assert bstTree.get_root() is None




def test_get_successor_node_with_right_child(bstTree):
    bstTree.insert(5)
    bstTree.insert(3)
    bstTree.insert(7)
    bstTree.insert(6)
    node = bstTree.search(5)
    successor = bstTree.get_successor(node)
    assert successor.get_data() == 6




