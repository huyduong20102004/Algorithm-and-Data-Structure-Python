class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None

    # Get height of node
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    # Get balance factor of node
    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Rotate right subtree rooted with y
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1

        return x

    # Rotate left subtree rooted with x
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1

        return y

    # Insert a node
    def insert(self, root, key):
        # Perform normal BST insertion
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height of this ancestor node
        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # Get the balance factor
        balance = self._balance(root)

        # If the node is unbalanced, then balance it
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    # Delete a node
    def delete(self, root, key):
        # Perform standard BST delete
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # Update height of the current node
        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # Get the balance factor
        balance = self._balance(root)

        # If the node is unbalanced, then balance it
        # Left Left Case
        if balance > 1 and self._balance(root.left) >= 0:
            return self._rotate_right(root)

        # Left Right Case
        if balance > 1 and self._balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Right Case
        if balance < -1 and self._balance(root.right) <= 0:
            return self._rotate_left(root)

        # Right Left Case
        if balance < -1 and self._balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    # Search for a node
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search(root.right, key)

        return self.search(root.left, key)

    # Get the node with minimum value
    def _min_value_node(self, node):
        current = node

        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    # Print the tree
    def preorder_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
# Tạo một cây AVL mới
avl_tree = AVLTree()

# Insert nodes
avl_tree.root = avl_tree.insert(avl_tree.root, 10)
avl_tree.root = avl_tree.insert(avl_tree.root, 20)
avl_tree.root = avl_tree.insert(avl_tree.root, 30)

# Print the tree
print("Preorder traversal of the AVL tree after insertion:")
avl_tree.preorder_traversal(avl_tree.root)
print()

# Delete node
avl_tree.root = avl_tree.delete(avl_tree.root, 20)

# Print the tree after deletion
print("Preorder traversal of the AVL tree after deletion:")
avl_tree.preorder_traversal(avl_tree.root)
print()

# Search for a node
key_to_search = 30
result = avl_tree.search(avl_tree.root, key_to_search)
if result:
    print(f"{key_to_search} found in the AVL tree.")
else:
    print(f"{key_to_search} not found in the AVL tree.")









