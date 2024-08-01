class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, color='BLACK')
        self.root = self.nil

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node == self.nil or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)


# Example usage:
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.root = Node(10)
    rb_tree.root.left = Node(5)
    rb_tree.root.right = Node(15)
    rb_tree.root.left.left = Node(3)
    rb_tree.root.left.right = Node(7)
    rb_tree.root.right.left = Node(13)
    rb_tree.root.right.right = Node(17)

    # Search for a key
    result = rb_tree.search(7)
    if result != rb_tree.nil:
        print("Key found!")
    else:
        print("Key not found!")
