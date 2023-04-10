from myLib.datastructures.linear.LLStack import Stack
from myLib.datastructures.linear.singlyLL import SinglyLinkedList
#from myLib.datastructures.linear.singlyCLL import CircularSinglyLinkedList

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
    print('singlyCLL TESTING BEGAN')






if __name__ == '__main__':
    main()



