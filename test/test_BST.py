import unittest
from final338proj.myLib.datastructures.trees.BST import BST
from final338proj.myLib.datastructures.nodes.TNode import TNode
from queue import Queue

class BSTTestCase(unittest.TestCase):
    def setUp(self):
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

if __name__ == '__main__':
    unittest.main()