from myLib.datastructures.trees.AVL import AVL
from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.trees.BST import BST

import pytest

@pytest.fixture
def avl():
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(3)
    avl.insert(7)
    avl.insert(13)
    avl.insert(17)
    return avl

def test_insert(avl):
    assert avl.get_root().get_val() == 10
    assert avl.get_root().get_left().get_val() == 5
    assert avl.get_root().get_right().get_val() == 15
    assert avl.get_root().get_left().get_left().get_val() == 3
    assert avl.get_root().get_left().get_right().get_val() == 7
    assert avl.get_root().get_right().get_left().get_val() == 13
    assert avl.get_root().get_right().get_right().get_val() == 17
