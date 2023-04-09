 
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.linear.singlyCLL import CircularSinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
import myLib.datastructures.linear.singlyLL
##from myLib.datastructures.nodes.DNode import DNode

print('SINGLYLL TESTING BEGAN')
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



def main():
    # create a linked list
    linked_list = SinglyLinkedList()

    # insert some nodes
    linked_list.insert_head(SNode(1))
    linked_list.insert_head(SNode(2))
    linked_list.insert_head(SNode(3))
    linked_list.insert_head(SNode(4))

    # print the list
    linked_list.Print()

    # search for a value
    node = linked_list.Search(3)
    if node is not None:
        print(f"Found node with value {node.value}")
    else:
        print("Value not found")

    # delete a node
    node = linked_list.Search(2)
    if node is not None:
        linked_list.Delete(node)
        print(f"Deleted node with value {node.value}")
    else:
        print("Value not found")

    # print the list again
    linked_list.Print()

    # clear the list
    linked_list.Clear()
    linked_list.Print()

    # test edge cases
    # insert a node at position 0
    linked_list.insert(SNode(5), 0)
    linked_list.Print()

    # insert a node at position 2
    linked_list.insert(SNode(6), 2)
    linked_list.Print()

    # insert a node at position 100 (should insert at tail)
    linked_list.insert(SNode(7), 100)
    linked_list.Print()
    print('TEST1')
    # Edge case 1: Inserting a node at position 0 in an empty list
    lst = SinglyLinkedList()
    assert lst.length == 0
    assert lst.head == None
    assert lst.tail == None
    assert lst.sorted == True
    lst.Print()

# test case 2: creating a list with one element and performing operations on it\
    print('TEST 2')
    node = SNode(1)
    lst.insert_head(node)
    assert lst.length == 1
    assert lst.head == node
    assert lst.tail == node
    assert lst.sorted == True
    lst.Print()
    print('TEST 3')
# test case 3: creating a list with multiple elements and performing operations on it
    node2 = SNode(2)
    node3 = SNode(3)
    lst.insert_tail(node2)
    lst.insert_tail(node3)
    assert lst.length == 3
    assert lst.head == node
    assert lst.tail == node3
    assert lst.sorted == True
    lst.Print()

    print('TEST 4')
    # test case 4: creating a sorted list and performing operations on it
    lst2 = SinglyLinkedList()
    node4 = SNode(1)
    node5 = SNode(2)
    node6 = SNode(3)
    lst2.SortedInsert(node5)
    print(lst2.length)  # expect 1
    lst2.Print()  # expect 2 -> None -> None
    lst2.SortedInsert(node4)
    print(lst2.length)  # expect 2
    lst2.Print()  # expect 1 -> 2 -> None
    lst2.SortedInsert(node6)
    print(lst2.length)  # expect 3
    lst2.Print()  # expect 1 -> 2 -> 3 -> None

    print('TEST 6')
    # test case 6: performing operations on a list with duplicate elements
    lst4 = SinglyLinkedList()
    node10 = SNode(1)
    node11 = SNode(2)
    node12 = SNode(2)
    lst4.insert_tail(node10)
    lst4.insert_tail(node11)
    lst4.insert_tail(node12)
    assert lst4.length == 3
    assert lst4.head == node10
    assert lst4.tail == node12
    assert lst4.sorted == True
    lst4.Print()
    print('TEST 7')
# test case 7: performing operations on a list with elements of different data types
    lst5 = SinglyLinkedList()
    node13 = SNode(1)
    node14 = SNode("hello")
    node15 = SNode(3.14)
    lst5.insert_tail(node13)
    lst5.insert_tail(node14)
    lst5.insert_tail(node15)
    assert lst5.length == 3
    assert lst5.head == node13
    lst5.Print()

    print('SINGLYLL TESTING DONE')


    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    node4 = SNode(4)

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





if __name__ == '__main__':
    main()



