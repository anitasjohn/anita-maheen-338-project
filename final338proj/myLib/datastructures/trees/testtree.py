from BST import BST
from TNode import TNode
from AVL import AVL

tree1 = BST()
print(tree1.get_root())  # Output: None

tree2 = BST(5)
print(tree2.get_root())  # Output: 5

node1 = TNode(10)
node2 = TNode(20)
node3 = TNode(30)
node4 = TNode(40)

node1.set_left(node2)
node1.set_right(node3)
node2.set_right(node4)

tree3 = BST(node1)
print(tree3.get_root())  # Output: 10

tree3.insert(15)
tree3.insert(5)
tree3.insert(25)

node5 = tree3.search(15)
print(node5.get_data())  # Output: 15

tree3.delete(20)
node6 = tree3.search(20)
print(node6)  # Output: None

tree3.print_in_order()  # Output: 5 10 15 25 30

tree3.print_bf()

## for avl specifically

avl_tree = AVL()

avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(50)
avl_tree.insert(25)

print("Inorder traversal of AVL tree:")
avl_tree.print_in_order()

print("\nBreadth-first traversal of AVL tree:")
avl_tree.print_bf()

avl_tree.delete(30)

print("\nInorder traversal of AVL tree after deleting 30:")
avl_tree.print_in_order()

print("\nBreadth-first traversal of AVL tree after deleting 30:")
avl_tree.print_bf()