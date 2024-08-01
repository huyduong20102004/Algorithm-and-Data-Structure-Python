class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(current_level)

    return result

# Constructing the tree
"""
        F
       / \
      B   G
     / \   \
    A   D   I
       / \   
      C   E  
         /
        H
"""
root = TreeNode('F')
root.left = TreeNode('B')
root.right = TreeNode('G')
root.left.left = TreeNode('A')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')
root.left.right.right.left = TreeNode('H')  
root.right.right = TreeNode('I')

print("Level-order traversal of the tree:")
print(", ".join(levelOrderTraversal(root)))


