#  Give the preorder, inorder, postorder, and level-order traversals of the following binary trees.
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root is None:
        return []
    result = []
    result.append(root.val)
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    return result


def inorder_traversal(root):
    if root is None:
        return []
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result


def postorder_traversal(root):
    if root is None:
        return []
    result = []
    result.extend(postorder_traversal(root.left))
    result.extend(postorder_traversal(root.right))
    result.append(root.val)
    return result


def level_order_traversal(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# Example binary tree
"""
        1
       / \
      2   3
     / \
    4   5
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder traversal:", preorder_traversal(root))
print("Inorder traversal:", inorder_traversal(root))
print("Postorder traversal:", postorder_traversal(root))
print("Level-order traversal:", level_order_traversal(root))
