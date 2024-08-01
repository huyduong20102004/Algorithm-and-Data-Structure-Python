class TreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = TreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = TreeNode()
            new_root.children.insert(0, root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, k)
            self.root = new_root
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = TreeNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t - 1]

    def search(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search(k, x.children[i])
        else:
            return self.search(k, self.root)

    def delete(self, k):
        result = self.search(k)
        if result:
            (node, index) = result
            if node is not None:
                if node.leaf:
                    del node.keys[index]
                else:
                    pass  # Handling deletion from non-leaf nodes
        else:
            print(f"Key {k} not found in the B-tree.")


# Example usage:
b_tree = BTree(3)

# Insert some keys
keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17, 3]
for key in keys_to_insert:
    b_tree.insert(key)

# Search for a key
search_key = 6
result = b_tree.search(search_key)
if result:
    print(f"Key {search_key} found in the B-tree.")
else:
    print(f"Key {search_key} not found in the B-tree.")

# Delete a key
delete_key = 6
b_tree.delete(delete_key)
print(f"Key {delete_key} deleted from the B-tree.")

# Search for the deleted key again
result = b_tree.search(delete_key)
if result:
    print(f"Key {delete_key} found in the B-tree.")
else:
    print(f"Key {delete_key} not found in the B-tree.")


