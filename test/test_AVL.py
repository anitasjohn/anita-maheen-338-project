from myLib.datastructures.trees.AVL import AVL
from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.trees.BST import BST

import pytest

@pytest.fixture
def empty_avl():
    return AVL()
# Define a fixture to create a sample AVL tree
@pytest.fixture
def avl_tree():
    root = TNode(5)
    avl = AVL(root)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    return avl

@pytest.fixture
def filled_avl():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(3)
    avl.insert(7)
    avl.insert(12)
    avl.insert(17)
    avl.insert(1)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    avl.insert(11)
    avl.insert(13)
    avl.insert(16)
    avl.insert(18)
    return avl
def test_avl_insert(empty_avl):
    empty_avl.insert(5)
    assert empty_avl.get_root().get_data() == 5
    empty_avl.insert(3)
    assert empty_avl.get_root().get_left().get_data() == 3
    empty_avl.insert(7)
    assert empty_avl.get_root().get_right().get_data() == 7
    empty_avl.insert(1)
    assert empty_avl.get_root().get_left().get_left().get_data() == 1
    empty_avl.insert(4)
    assert empty_avl.get_root().get_left().get_right().get_data() == 4
    empty_avl.insert(6)
    assert empty_avl.get_root().get_right().get_left().get_data() == 6
    empty_avl.insert(8)
    assert empty_avl.get_root().get_right().get_right().get_data() == 8
def test_avl_insert_node(empty_avl):
    node = TNode(5)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_data() == 5
    node = TNode(3)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_left().get_data() == 3
    node = TNode(7)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_right().get_data() == 7
    node = TNode(1)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_left().get_left().get_data() == 1
    node = TNode(4)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_left().get_right().get_data() == 4
    node = TNode(6)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_right().get_left().get_data() == 6
    node = TNode(8)
    empty_avl.insert_node(node)
    assert empty_avl.get_root().get_right().get_right().get_data() == 8
def test_avl_balance_tree(filled_avl):
    root = filled_avl.get_root()
    assert root.get_balance() == 0
    left = root.get_left()
    assert left.get_balance() == 0
    left_left = left.get_left()
    assert left_left.get_balance() == 0
    left_right = left.get_right()
    assert left_right.get_balance() == 0
    right = root.get_right()
    assert right.get_balance() == 0
    right_left = right.get_left()
    assert right_left.get_balance() == 0
    right_right = right.get_right()

def test_insert():
    # Create an empty AVL tree
    avl_tree = AVL()
    
    # Insert some values into the tree
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    
    # Check that the tree now contains the values
    assert avl_tree.search(10) is not None
    assert avl_tree.search(20) is not None
    assert avl_tree.search(30) is not None
def test_delete():
    # Create an AVL tree with some values
    avl_tree = AVL(TNode(20))
    avl_tree.insert(10)
    avl_tree.insert(30)
    
    # Delete a value from the tree
    avl_tree.delete(10)
    
    # Check that the value is no longer in the tree
    assert avl_tree.search(10) is None

def test_rotate_left():
    # Create an AVL tree with an unbalanced node
    avl_tree = AVL(TNode(10))
    avl_tree.insert(5)
    avl_tree.insert(15)
    avl_tree.insert(20)
    
    # Rotate left at the unbalanced node
    avl_tree.rotate_left(avl_tree.root)
    
    # Check that the tree is now balanced
    assert avl_tree.root.get_data() == 15
    assert avl_tree.root.get_left().get_data() == 10
    assert avl_tree.root.get_right().get_data() == 20



    
def test_insertion(avl_tree):
    # Check if the root node is balanced after insertion
    assert avl_tree.get_root().get_balance() == 0

    # Check if the left and right child nodes are balanced after insertion
    assert avl_tree.get_root().get_left().get_balance() == 0
    assert avl_tree.get_root().get_right().get_balance() == 0
def test_empty_avl_tree():
    avl = AVL()
    assert avl.get_root() is None
def test_avl_tree_single_node():
    avl = AVL(TNode(5))
    assert avl.get_root().get_data() == 5
def test_avl_tree_insert():
    avl = AVL(TNode(5))
    avl.insert(3)
    assert avl.get_root().get_data() == 5
    assert avl.get_root().get_left().get_data() == 3

def test_avl_tree_delete_nonexistent():
    avl = AVL(TNode(5))
    avl.insert(3)
    avl.insert(7)
    avl.delete(9)
    assert avl.get_root().get_data() == 5
    assert avl.get_root().get_left().get_data() == 3
    assert avl.get_root().get_right().get_data() == 7
def test_avl_tree_insert_and_delete():
    avl = AVL(TNode(5))
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    avl.delete(5)
    assert avl.get_root().get_data() == 6
    assert avl.get_root().get_left().get_data() == 3
    assert avl.get_root().get_left().get_left().get_data() == 2
    assert avl.get_root().get_left().get_right().get_data() == 4
    assert avl.get_root().get_right().get_data() == 7
    assert avl.get_root().get_right().get_right().get_data() == 8
