from node import DNode
'''from doublyCLL import CircularDoublyLinkedList

# test insert_head method
dll = CircularDoublyLinkedList()
node1 = DNode(1)
node2 = DNode(2)
dll.insert_head(node1)
dll.insert_head(node2)
print(dll.head.value)
print(dll.tail.value)
print(dll.head.next.value)
print(dll.tail.previous.value)
assert dll.head == node2
assert dll.tail == node1
assert dll.head.next == node1
assert dll.tail.previous == node2

# test insert_tail method
dll = CircularDoublyLinkedList()
node1 = DNode(1)
node2 = DNode(2)
dll.insert_tail(node1)
dll.insert_tail(node2)
print(dll.head.value)
print(dll.tail.value)
print(dll.head.next.value)
print(dll.tail.previous.value)
assert dll.head == node1
assert dll.tail == node2
assert dll.head.next == node2
assert dll.tail.previous == node1

# test insert method
dll = CircularDoublyLinkedList()
node1 = DNode(1)
node2 = DNode(2)
node3 = DNode(3)
dll.insert_head(node1)
dll.insert_tail(node3)
dll.insert(node2, 1)
print(dll.head.value)
print(dll.tail.value)
print(dll.head.next.value)
print(dll.tail.previous.value)
print(dll.head.next.next.value)
print(dll.tail.previous.previous.value)
assert dll.head == node1
assert dll.tail == node3
assert dll.head.next == node2
assert dll.tail.previous == node2
assert dll.head.next.next == node3
assert dll.tail.previous.previous == node1

# test DeleteHead method
dll = CircularDoublyLinkedList()
node1 = DNode(1)
node2 = DNode(2)
dll.insert_head(node1)
dll.insert_tail(node2)
dll.DeleteHead()
print(dll.head.value)
print(dll.tail.value)
print(dll.head.previous.value)
print(dll.tail.next.value)
assert dll.head == node2
assert dll.tail == node2
assert dll.head.previous == node2
assert dll.tail.next == node2

# test DeleteTail method
dll = CircularDoublyLinkedList()
node1 = DNode(1)
node2 = DNode(2)
dll.insert_head(node1)
dll.insert_tail(node2)
dll.DeleteTail()
print(dll.head.value)
print(dll.tail.value)
print(dll.head.previous.value)
print(dll.tail.next.value)
assert dll.head == node1
assert dll.tail == node1
assert dll.head.previous == node1
assert dll.tail.next == node1

# test Delete method
dll = CircularDoublyLinkedList()
node1 = DNode(1)
node2 = DNode(2)
node3 = DNode(3)
dll.insert_head(node1)
dll.insert_tail(node3)
dll.insert(node2, 1)
dll.Delete(node2)
print(dll.head.value)
print(dll.tail.value)
print(dll.head.next.value)
print(dll.tail.previous.value)
assert dll.head == node1
assert dll.tail == node3
assert dll.head.next == node3
assert dll.tail.previous == node1'''














'''from singlyCLL import CircularSinglyLinkedList

# create some nodes to add to the list
node1 = DNode(1)
node2 = DNode(2)
node3 = DNode(3)

# create an instance of the CircularSinglyLinkedList class
my_list = CircularSinglyLinkedList()

# insert nodes into the list
my_list.insert_head(node1)
my_list.insert_tail(node2)
my_list.insert_tail(node3)

# print the list
my_list.Print()  # expected output: 1 2 3

# delete the head and tail nodes
my_list.DeleteHead()
my_list.DeleteTail()

# print the list again
my_list.Print()  # expected output: 2

# try deleting the head and tail nodes again
my_list.DeleteHead()  # expected output: None
my_list.DeleteTail()  # expected output: 2

# print the list one last time
my_list.Print()  # expected output: 
                 # List length: 0
                 # List content:'''








"""from doublyLL import DoublyLinkedList



# create a new instance of the DoublyLinkedList class
dll = DoublyLinkedList()

# create some DNode instances to insert into the list
node1 = DNode(1)
node2 = DNode(2)
node3 = DNode(3)

# insert nodes into the list
dll.insert_head(node1)
dll.insert_tail(node2)
dll.insert(node3, 1)

# print the contents of the list
curr = dll.head
while curr is not None:
    print(curr.value)
    curr = curr.next

# delete a node from the list
dll.Delete(node2)

# print the contents of the list again
curr = dll.head
while curr is not None:
    print(curr.value)
    curr = curr.next"""



"""from node import Node
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
my_list.Print()"""
