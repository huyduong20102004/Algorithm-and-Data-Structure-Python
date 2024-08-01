class PropertyTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = {}

class PropertyTree:
    def __init__(self):
        self.root = PropertyTreeNode(None, None)

    def insert(self, key_path, value):
        current_node = self.root
        for key in key_path:
            if key not in current_node.children:
                current_node.children[key] = PropertyTreeNode(key, None)
            current_node = current_node.children[key]
        current_node.value = value

    def search(self, key_path):
        current_node = self.root
        for key in key_path:
            if key not in current_node.children:
                return None
            current_node = current_node.children[key]
        return current_node.value

    def delete(self, key_path):
        nodes = [self.root]
        for key in key_path:
            if key not in nodes[-1].children:
                return  # Key path not found
            nodes.append(nodes[-1].children[key])

        # Remove the value at the last node
        nodes[-1].value = None

        # Remove any intermediate nodes with no children or values
        for i in range(len(nodes) - 1, 0, -1):
            if nodes[i].children or nodes[i].value is not None:
                break
            del nodes[i - 1].children[key_path[i - 1]]

# Example usage:
prop_tree = PropertyTree()

# Inserting values
prop_tree.insert(["user", "name"], "John")
prop_tree.insert(["user", "age"], 30)
prop_tree.insert(["settings", "theme"], "dark")

# Searching for values
print(prop_tree.search(["user", "name"]))  # Output: John
print(prop_tree.search(["settings", "theme"]))  # Output: dark

# Deleting a value
prop_tree.delete(["user", "age"])
print(prop_tree.search(["user", "age"]))  # Output: None



