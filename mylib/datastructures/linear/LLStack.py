from node import Node
from singlyLL import SinglyLinkedList
class Stack(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    # Override methods from SinglyLinkedList that do not apply to Stacks
    def insert_tail(self, node):
        pass
    
    def insert(self, node, position):
        pass
    
    def SortedInsert(self, node):
        pass
    
    def isSorted(self):
        return True
    
    def Search(self, value):
        pass
    
    # Add new methods specific to Stack functionality
    def push(self, node):
        super().insert_head(node)
    
    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value
    
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.value
