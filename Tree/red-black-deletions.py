class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = "RED"  # Initial color is always red


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)  # Sentinel node
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key)
        new_node.parent = None
        new_node.key = key
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = "RED"

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent == None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent == None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def delete(self, key):
        node = self.find_node(key)
        if node == self.NIL:
            print("Node not found")
            return
        self.delete_node(node)

    def delete_node(self, node):
        if node.left != self.NIL and node.right != self.NIL:
            successor = self.find_min(node.right)
            node.key = successor.key
            node = successor

        child = node.left if node.left != self.NIL else node.right
        self.transplant(node, child)

        if node.color == "BLACK":
            self.fix_double_black(child)

    def fix_double_black(self, node):
        while node != self.root and node.color == "BLACK":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == "BLACK" and sibling.left.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.left.color == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = "BLACK"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def find_node(self, key):
        current = self.root
        while current != self.NIL:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return self.NIL

    def find_min(self, node):
        current = node
        while current.left != self.NIL:
            current = current.left
        return current

    def print_tree(self):
        self.print_helper(self.root, "", True)

    def print_helper(self, node, indent, last):
        if node != self.NIL:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            color = "RED" if node.color == "RED" else "BLACK"
            print(node.key, "(", color, ")", sep="")
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)


# Sử dụng cây Red-Black
tree = RedBlackTree()

# Thêm các node vào cây
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(25)

# Hiển thị cây trước khi xóa node
print("Cây trước khi xóa node:")
tree.print_tree()

# Xóa một node
tree.delete(20)

# Hiển thị cây sau khi xóa node
print("Cây sau khi xóa node:")
tree.print_tree()





