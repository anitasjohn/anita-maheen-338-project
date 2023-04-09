from myLib.datastructures.linear.singlyCLL import CircularSinglyLinkedList

# Test creation of an empty circular singly linked list
csll = CircularSinglyLinkedList()
assert csll.length == 0 # Expected length is 0

# Test insertion of a node at the head of the list
csll.insert_head(node1)
assert csll.length == 1 # Expected length is 1
assert csll.head == node1 # Expected head node is node1
assert csll.tail == node1 # Expected tail node is node1

# Test insertion of a second node at the head of the list
csll.insert_head(node2)
assert csll.length == 2 # Expected length is 2
assert csll.head == node2 # Expected head node is node2
assert csll.tail == node1 # Expected tail node is node1

# Test insertion of a node at the tail of the list
csll.insert_tail(node3)
assert csll.length == 3 # Expected length is 3
assert csll.head == node2 # Expected head node is node2
assert csll.tail == node3 # Expected tail node is node3

# Test insertion of a second node at the tail of the list
csll.insert_tail(node4)
assert csll.length == 4 # Expected length is 4
assert csll.head == node2 # Expected head node is node2
assert csll.tail == node4 # Expected tail node is node4

# Test deletion of the head node
deleted_node = csll.DeleteHead()
assert deleted_node == 2 # Expected deleted node value is 2
assert csll.length == 3 # Expected length is 3
assert csll.head == node1 # Expected head node is node1
assert csll.tail == node4 # Expected tail node is node4

# Test deletion of the tail node
deleted_node = csll.DeleteTail()
assert deleted_node == 4 # Expected deleted node value is 4
assert csll.length == 2 # Expected length is 2
assert csll.head == node1 # Expected head node is node1
assert csll.tail == node3 # Expected tail node is node3

