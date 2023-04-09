 
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
'''
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
'''


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
    # Edge case 1: Inserting a node at position 0 in an empty list
list1 = SinglyLinkedList()
node1 = SNode(10)
list1.insert(node1, 0)
list1.Print()  # Expected output: List length: 1, Sorted status: True, List content: 10

# Edge case 2: Inserting a node at a position greater than or equal to the length of the list
list2 = SinglyLinkedList()
node2 = SNode(20)
list2.insert_head(node2)
node3 = SNode(30)
list2.insert(node3, 2)
list2.Print()  # Expected output: List length: 2, Sorted status: True, List content: 20 30

# Edge case 3: Deleting the only node in a list
list3 = SinglyLinkedList()
node4 = SNode(40)
list3.insert_head(node4)
list3.DeleteHead()
list3.Print()  # Expected output: List length: 0, Sorted status: True, List content:

# Edge case 4: Deleting the tail of a list with only two nodes
list4 = SinglyLinkedList()
node5 = SNode(50)
node6 = SNode(60)
list4.insert_head(node5)
list4.insert_tail(node6)
list4.DeleteTail()
list4.Print()  # Expected output: List length: 1, Sorted status: True, List content: 50

# Edge case 5: Deleting a node that is not in the list
list5 = SinglyLinkedList()
node7 = SNode(70)
node8 = SNode(80)
list5.insert_head(node7)
list5.insert_tail(node8)
node9 = SNode(90)
list5.Delete(node9)
list5.Print()  # Expected output: List length: 2, Sorted status: True, List content: 70 80


if __name__ == '__main__':
    main()
