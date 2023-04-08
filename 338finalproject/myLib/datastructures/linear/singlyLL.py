import os
import sys

# get the path to the nodes directory
nodes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'nodes'))
sys.path.append(nodes_path)

# import SNode from the nodes directory
from SNode import SNode













class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sorted = True
        self.length = 0
        
    def insert_head(self, node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.length += 1
    
    def insert_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        elif position >= self.length:
            self.insert_tail(node)
        else:
            curr = self.head
            for i in range(position-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
            self.length += 1

    def SortedInsert(self, node):
        if self.head is None:  # if list is empty, insert at head
            self.insert_head(node)
            return

        # check if list is sorted
        if not self.sorted:
            self.Sort()  # if not sorted, sort the list before inserting

        # insert node at proper position
        current = self.head
        prev = None
        while current is not None and current.data < node.data:
            prev = current
            current = current.next

        if prev is None:
            self.insert_head(node)
        else:
            node.next = current
            prev.next = node

        self.length += 1
    
    def isSorted(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def Search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None



    def DeleteHead(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
    
    def DeleteTail(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            value = self.tail.data
            self.head = None
            self.tail = None
            return value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            value = self.tail.data
            self.tail = current_node
            self.tail.next = None
            return value
    
    def Delete(self, node):
        if self.head == None:
            return None
        elif self.head == node:
            self.head = node.next
            return node.value
        else:
            current_node = self.head
        while current_node.next != node:
            current_node = current_node.next
        if current_node.next == None:
            return None
        else:
            current_node.next = node.next
            return node.value


    def Clear(self):
        """Deletes the whole list."""
        self.head = None
        self.tail = None
        self.sorted = True
        self.length = 0

    def Print(self):
        """Prints the list information on the screen."""
        print("List length:", self.length)
        print("Sorted status:", self.sorted)
        print("List content:")
        current = self.head
        while current:
            print(current.value)
            current = current.next

