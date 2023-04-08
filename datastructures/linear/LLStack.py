
import sys
sys.path.append("C:/Users/anita/OneDrive/Documents/GitHub/anita-maheen-338-project/datastructures")
from nodes.SNode import SNode


from singlyLL import SinglyLinkedList

class Stack(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    # override methods from SinglyLinkedList that do not apply to stack behavior
    def insert_tail(self, node):
        pass

    def insert(self, node, position):
        pass

    def sortedInsert(self, node):
        pass

    # define wrappers with proper naming conventions for stack functionality
    def push(self, node):
        super().insert_head(node)

    def pop(self):
        value = self.head.value
        self.DeleteHead()
        return value

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.length == 0
