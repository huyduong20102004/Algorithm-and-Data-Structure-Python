class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = "red"  # New nodes are always red by default

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.root.color = "black"  # Root is always black
            return

        # Insert the node like in a regular binary search tree
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the properties of the red-black tree after insertion
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "red":
                    # Case 1: Uncle is red
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is a right child
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: Node is a left child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "red":
                    # Case 1: Uncle is red
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Node is a left child
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: Node is a right child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)

        self.root.color = "black"  # Ensure the root is black

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, node.color)
            self.inorder_traversal(node.right)

# Example usage:
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
rb_tree.insert(15)
rb_tree.insert(25)
rb_tree.insert(5)
rb_tree.insert(35)

print("Inorder Traversal:")
rb_tree.inorder_traversal(rb_tree.root)




