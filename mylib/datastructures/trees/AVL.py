from TNode import TNode
from BST import BST

class AVL(BST):
    def __init__(self):
        self.root = None
    
    def __init__(self, val):
        self.root = TNode(val)
    
    def __init__(self, obj):
        self.root = obj
        if obj.left_child is not None or obj.right_child is not None:
            self.root = self.balance_tree(obj)