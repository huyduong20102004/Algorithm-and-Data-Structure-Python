class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")  # In ra giá trị của nút hiện tại
        preorder_traversal(node.left)  # Duyệt qua cây con bên trái
        preorder_traversal(node.right)  # Duyệt qua cây con bên phải

# Ví dụ về cấu trúc cây
#       A
#      / \
#     B   C
#    / \
#   D   E

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

print("Pre-order traversal of the tree:", end=" ")
preorder_traversal(root)
