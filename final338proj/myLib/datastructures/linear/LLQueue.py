from myLib.datastructures.linear.singlyLL import SinglyLinkedList


class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        
    def enqueue(self, node):
        """Inserts the node at the tail of the queue."""
        super().insert_tail(node)
        
    def dequeue(self):
        """Removes and returns the node at the head of the queue."""
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = node.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return node.value
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.value
        
    # Override methods that are not applicable to queue with empty body methods
    def SortedInsert(self, node):
        pass
    
    def isSorted(self):
        pass
    
    def Search(self, value):
        pass
    
    def DeleteHead(self):
        pass
    
    def DeleteTail(self):
        pass
    
    def Delete(self, node):
        pass
