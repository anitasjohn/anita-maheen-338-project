from final338proj.myLib.datastructures.nodes.TNode import TNode
from BST import BST
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

print("In order:")
tree3.print_in_order()  # Output: 5 10 15 25 30

print("Breadth-first, with each level on a new line:")
tree3.print_bf()

##avl = AVL()
##print("Root node of default AVL tree:", avl.root)

"""

avl = AVL(50)
print("Root node of AVL tree with root value 50:", avl.root.get_data())

t = TNode(50)
t.set_left(TNode(30))
t.set_right(TNode(80))
avl = AVL(t)
print("Root node of balanced AVL tree from passed tree:", avl.root.get_data())

avl.insert(40)
avl.insert(70)
avl.insert(60)
avl.insert(20)
avl.insert(10)
avl.insert(90)
print("In-order traversal of AVL tree after insertions:")
avl.print_in_order()

avl.delete(20)
avl.delete(50)
print("In-order traversal of AVL tree after deletions:")
avl.print_in_order()

node = avl.search(60)
print("Node with value 60:", node.get_data())

print("Balances of nodes in AVL tree:")
avl.print_bf()

## for avl tree specifically

avl_tree = AVL(10)

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

"""