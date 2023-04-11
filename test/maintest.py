from myLib.datastructures.linear.LLStack import Stack
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.linear.singlyCLL import CircularSinglyLinkedList
from myLib.datastructures.linear.LLStack import Stack

from myLib.datastructures.nodes.SNode import SNode
import myLib.datastructures.linear.singlyLL
##from myLib.datastructures.nodes.DNode import DNode


def main():
    print('SINGLYLL TESTING BEGAN')


# Test insert_head() method
    print("Test insert_head() method:")
    lst = SinglyLinkedList()
    lst.insert_head(SNode(3))
    lst.insert_head(SNode(2))
    lst.insert_head(SNode(1))
    lst.Print()  # Output: 1 -> 2 -> 3 -> None

# Test insert_tail() method
    print("Test insert_tail() method:")
    lst = SinglyLinkedList()
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.insert_tail(SNode(3))
    lst.Print()  # Output: 1 -> 2 -> 3 -> None

# Test insert() method
    print("Test insert() method:")
    lst = SinglyLinkedList()
    lst.insert(SNode(1), 0)  # Insert at head
    lst.insert(SNode(3), 1)  # Insert at tail
    lst.insert(SNode(2), 1)  # Insert in middle
    lst.Print()  # Output: 1 -> 2 -> 3 -> None

# Test SortedInsert() method
    print("Test SortedInsert() method:")
    lst = SinglyLinkedList()
    lst.SortedInsert(SNode(2))
    lst.SortedInsert(SNode(1))
    lst.SortedInsert(SNode(3))
    lst.Print()  # Output: 1 -> 2 -> 3 -> None

# Test DeleteHead() method
    print("Test DeleteHead() method:")
    lst = SinglyLinkedList()
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.DeleteHead()
    lst.Print()  # Output: 2 -> None

# Test DeleteTail() method
    print("Test DeleteTail() method:")
    lst = SinglyLinkedList()
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.DeleteTail()
    lst.Print()  # Output: 1 -> None

# Test Delete() method
    print("Test Delete() method:")
    lst = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    lst.insert_tail(node1)
    lst.insert_tail(node2)
    lst.insert_tail(node3)
    lst.Delete(node2)
    lst.Print()  # Output: 1 -> 3 -> None

# Test Clear() method
    print("Test Clear() method:")
    lst = SinglyLinkedList()
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.Clear()
    lst.Print()  # Output: List is empty

# Test Search() method
    print("Test Search() method:")
    lst = SinglyLinkedList()
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.insert_tail(SNode(3))
    node = lst.Search(2)
    print(node.value)  # Output: 2

# Test isSorted() method
    print("Test isSorted() method:")
    lst = SinglyLinkedList()
    lst.insert_tail(SNode(1))
    lst.insert_tail(SNode(2))
    lst.insert_tail(SNode(3))
    print(lst.isSorted())  # Output: True
    lst.insert_tail(SNode(1))
    print(lst.isSorted())  # Output: False
    lst.Sort()
    print(lst.isSorted())  # Output: True


    # Create a new linked list
    ll = SinglyLinkedList()

# Insert nodes at the head
    ll.insert_head(SNode(5))
    ll.insert_head(SNode(3))
    ll.insert_head(SNode(7))
    ll.insert_head(SNode(1))

# Insert nodes at the tail
    ll.insert_tail(SNode(9))
    ll.insert_tail(SNode(2))
    ll.insert_tail(SNode(4))



# Insert a node in sorted order
    ll.SortedInsert(SNode(8))

# Search for a node
    node = ll.Search(7)
    if node is not None:
        print("Found node with value", node.value)
    else:
        print("Node not found")

# Delete the head and tail nodes
    ll.DeleteHead()
    ll.DeleteTail()

# Delete a specific node
    node = ll.Search(6)
    if node is not None:
        ll.Delete(node)

# Sort the list
    ll.Sort()

# Print the list
    ll.Print()

# Clear the list
    ll.Clear()

    print('SINGYLL TESTING END')
    print('-----------------------------')
    print('singlyCLL TESTING BEGIN')
    print('TEST 1')
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    node4 = SNode(4)
# Test creation of an empty circular singly linked list
    csll = CircularSinglyLinkedList()
    assert csll.length == 0 # Expected length is 0
    print('TEST 2')
# Test insertion of a node at the head of the list
    csll.insert_head(node1)
    assert csll.length == 1 # Expected length is 1
    assert csll.head == node1 # Expected head node is node1
    assert csll.tail == node1 # Expected tail node is node1
    print('TEST 3')
# Test insertion of a second node at the head of the list
    csll.insert_head(node2)
    assert csll.length == 2 # Expected length is 2
    assert csll.head == node2 # Expected head node is node2
    assert csll.tail == node1 # Expected tail node is node1
    print('TEST 4')
# Test insertion of a node at the tail of the list
    csll.insert_tail(node3)
    assert csll.length == 3 # Expected length is 3
    assert csll.head == node2 # Expected head node is node2
    assert csll.tail == node3 # Expected tail node is node3
    print('TEST 5')
# Test insertion of a second node at the tail of the list
    csll.insert_tail(node4)
    assert csll.length == 4 # Expected length is 4
    assert csll.head == node2 # Expected head node is node2
    assert csll.tail == node4 # Expected tail node is node4
    print('TEST 6')
# Test deletion of the head node
    deleted_node = csll.DeleteHead()
    assert deleted_node == 2 # Expected deleted node value is 2
    assert csll.length == 3 # Expected length is 3
    assert csll.head == node1 # Expected head node is node1
    assert csll.tail == node4 # Expected tail node is node4
    
    print('TEST 7')
# Test deletion of the tail node
    deleted_node = csll.DeleteTail()
    assert deleted_node == 4 # Expected deleted node value is 4
    assert csll.length == 2 # Expected length is 2
    assert csll.head == node1 # Expected head node is node1
    assert csll.tail == node3 # Expected tail node is node3

    print('TEST 8')
    # create a new empty circular singly linked list
    cll = CircularSinglyLinkedList()

    # insert some nodes at the head
    cll.insert_head(SNode(1))
    cll.insert_head(SNode(2))
    cll.insert_head(SNode(3))

    # insert some nodes at the tail
    cll.insert_tail(SNode(4))
    cll.insert_tail(SNode(5))
    cll.insert_tail(SNode(6))

    # print the list
    cll.Print()

    # delete the head node
    print("Deleted head node:", cll.DeleteHead())

    # delete the tail node
    print("Deleted tail node:", cll.DeleteTail())

    # print the list again
    cll.Print()

    print('TEST 9')
    cll = CircularSinglyLinkedList()

    # test deleting from an empty list
    assert cll.DeleteHead() is None
    assert cll.DeleteTail() is None

    # insert a single node
    cll.insert_head(SNode(1))

    # test deleting the only node in the list
    assert cll.DeleteHead() == 1
    assert cll.DeleteTail() is None

    # insert multiple nodes
    cll.insert_head(SNode(2))
    cll.insert_head(SNode(3))
    cll.insert_tail(SNode(4))
    cll.insert_tail(SNode(5))

    # test deleting the head and tail nodes
    assert cll.DeleteHead() == 3
    assert cll.DeleteTail() == 5

    # print the list to confirm the remaining nodes
    cll.Print()
    # Expected output:
    # List length: 2
    # List content:
    # 2
    # 4
    print('TEST 10')
    # insert a node in an empty list
    cll = CircularSinglyLinkedList(SNode(1))
    assert cll.length == 1
    assert cll.head.value == 1
    assert cll.tail.value == 1
    print("Test Passed: Inserted node in an empty list.")
    print('TEST 11')
    # test inserting nodes at the head and tail of a one-node list
    cll.insert_head(SNode(2))
    cll.insert_tail(SNode(3))
    assert cll.head.value == 2
    assert cll.tail.value == 3
    assert cll.length == 3
    print("Test Passed: Inserted nodes at the head and tail of a one-node list.")
    print('singlyCLL TESTS DONE')
    print('-----------------------------')
    print('LLStack TESTING BEGIN')
    # create a new stack
    
   # Test SinglyLinkedList
    sll = SinglyLinkedList()
    sll.insert_head(SNode(1)) # Insert node with value 1 at the head
    sll.insert_head(SNode(2)) # Insert node with value 2 at the head
    sll.insert_head(SNode(3)) # Insert node with value 3 at the head
    print("Singly Linked List:")
    sll.Print() # Output: "3 -> 2 -> 1 -> None"
    print("Length:", sll.length) # Output: "Length: 3"

# Test Stack
    stack = Stack()
    stack.push(SNode(1)) # Push node with value 1 onto the stack
    stack.push(SNode(2)) # Push node with value 2 onto the stack
    stack.push(SNode(3)) # Push node with value 3 onto the stack
    print("\nStack:")
    print("Peek:", stack.peek()) # Output: "Peek: 3"
    print("Pop:", stack.pop()) # Output: "Pop: 3"
    print("Peek:", stack.peek()) # Output: "Peek: 2"
    print("Is empty?", stack.is_empty()) # Output: "Is empty? False"








if __name__ == '__main__':
    main()



