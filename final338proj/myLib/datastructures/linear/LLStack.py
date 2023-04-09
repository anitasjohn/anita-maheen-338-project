'''
import os
import sys

# get the path to the nodes directory
nodes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'nodes'))
sys.path.append(nodes_path)

# import SNode from the nodes directory
from SNode import SNode'''



from myLib.datastructures.linear.singlyLL import SinglyLinkedList

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
