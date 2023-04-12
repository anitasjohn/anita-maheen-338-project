from myLib.datastructures.linear.singlyLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode

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
        print(f"Before pop - head: {self.head}, length: {self.length}")
        value = self.head.value
        self.DeleteHead()
        print(f"After pop - head: {self.head}, length: {self.length}")
        if self.length == 0:
            self.head = None
        return value

    def peek(self):
        if self.head is not None:
            return self.head.value
        else:
            return None

    def is_empty(self):
        return self.length == 0