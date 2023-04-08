from TNode import TNode
from BST import BST


class AVL(BST):
    def __init__(self, root=None):
        super().__init__(root)

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root
        if root.get_left() is not None or root.get_right() is not None:
            self._rebalance_tree(root)

    def insert(self, val):
        super().insert(val)
        self.balance_tree()

    def insert_node(self, node):
        super().insert_node(node)
        self.balance_tree()

    def delete(self, val):
        node = self.search(val)
        if node is None:
            print("Value not found in the tree")
            return
        parent = node.get_parent()

        # Case 1: Node has no children
        if node.get_left() is None and node.get_right() is None:
            if parent is None:
                self.set_root(None)
            elif node == parent.get_left():
                parent.set_left(None)
            else:
                parent.set_right(None)
        # Case 2: Node has one child
        elif node.get_left() is None or node.get_right() is None:
            child = node.get_left() or node.get_right()
            if parent is None:
                self.set_root(child)
                child.set_parent(None)
            elif node == parent.get_left():
                parent.set_left(child)
                child.set_parent(parent)
            else:
                parent.set_right(child)
                child.set_parent(parent)
        # Case 3: Node has two children
        else:
            successor = self.get_successor(node)
            node.set_data(successor.get_data())
            self.delete(successor.get_data())

        self.balance_tree()

    def balance_factor(self, node):
        left_height = node.get_left().height() if node.get_left() else -1
        right_height = node.get_right().height() if node.get_right() else -1
        return right_height - left_height

    def balance_tree(self):
        node_stack = []
        curr = self.get_root()
        while True:
            if curr:
                node_stack.append(curr)
                curr = curr.get_left()
            elif node_stack:
                curr = node_stack.pop()
                balance_factor = self.balance_factor(curr)
                if balance_factor < -1:
                    if self.balance_factor(curr.get_left()) > 0:
                        self.rotate_left(curr.get_left())
                    self.rotate_right(curr)
                elif balance_factor > 1:
                    if self.balance_factor(curr.get_right()) < 0:
                        self.rotate_right(curr.get_right())
                    self.rotate_left(curr)
                curr = curr.get_right()
            else:
                break

    def rotate_right(self, node):
        pivot = node.get_left()
        if node == self.get_root():
            self.set_root(pivot)
            pivot.set_parent(None)
        else:
            parent = node.get_parent()
            if node == parent.get_left():
                parent.set_left(pivot)
            else:
                parent.set_right(pivot)
            pivot.set_parent(parent)
        node.set_left(pivot.get_right())
        if node.get_left():
            node.get_left().set_parent(node)
        pivot.set_right(node)
        node.set_parent(pivot)

    def rotate_left(self, node):
        pivot = node.get_right()
        if node == self.get_root():
            self.set_root(pivot)
            pivot.set_parent(None)
        else:
            parent = node.get_parent()
            if node == parent.get_left():
                parent.set_left(pivot)
            else:
                parent.set_right(pivot)
            pivot.set_parent(parent)
        node.set_right(pivot.get_left())
        if node.get_right():
            node.get_right().set_parent(node)
        pivot.set_left(node)
        node.set_parent(pivot)

