from node import Node
from singlyLL import SinglyLinkedList

# create an instance of SinglyLinkedList
my_list = SinglyLinkedList()

# create some nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(7)

# insert nodes into the list
my_list.insert_head(node1)
my_list.insert_tail(node2)
my_list.insert(node3, 1)

# print the list
my_list.Print()

# search for a node
result = my_list.Search(10)

if result:
    print("Node found:", result.value)
else:
    print("Node not found")

# delete a node
deleted_value = my_list.Delete(node1)
if deleted_value:
    print("Deleted node value:", deleted_value)
else:
    print("Node not found")

# print the updated list
my_list.Print()

# clear the list
my_list.Clear()

# print the empty list
my_list.Print()
