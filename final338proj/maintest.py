import myLib 

from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode

# create a new singly linked list
sll = SinglyLinkedList()

# insert some nodes into the list
node1 = SNode(5)
node2 = SNode(10)
node3 = SNode(15)
node4 = SNode(20)

sll.insert_head(node1)
sll.insert_tail(node2)
sll.insert(node3, 1)
sll.SortedInsert(node4)

# print the contents of the list
sll.Print()  # Expected output: 5 -> 10 -> 15 -> 20

# search for a node in the list
node = sll.Search(10)
if node is not None:
    print("Found node with value:", node.value)  # Expected output: Found node with value: 10
else:
    print("Node not found")

# delete a node from the list
sll.Delete(node3)

# print the updated contents of the list
sll.Print()  # Expected output: 5 -> 10 -> 20

# clear the list
sll.Clear()

# print the cleared list
sll.Print()  # Expected output: empty list

# create a new singly linked list
sll = SinglyLinkedList()

# insert some nodes into the list
node1 = SNode(5)
node2 = SNode(10)
node3 = SNode(15)
node4 = SNode(20)

sll.insert_head(node1)
sll.insert_tail(node2)
sll.insert(node3, 1)
sll.SortedInsert(node4)

# print the contents of the list
sll.Print()  # Expected output: 5 -> 10 -> 15 -> 20

# search for a node in the list
node = sll.Search(10)
if node is not None:
    print("Found node with value:", node.value)  # Expected output: Found node with value: 10
else:
    print("Node not found")

# delete a node from the list
sll.Delete(node3)

# print the updated contents of the list
sll.Print()  # Expected output: 5 -> 10 -> 20

# clear the list
sll.Clear()

# print the cleared list
sll.Print()  # Expected output: empty list
