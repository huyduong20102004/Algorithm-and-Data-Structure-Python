class Node:
    def __init__(self,value):
        self.value = value  # Giá trị của node
        self.left = None    # Node con bên trái (nếu có)
        self.right = None   # Node con bên phải (nếu có)

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)   # Duyệt node con bên trái
        post_order_traversal(node.right)  # Duyệt node con bên phải
        print(node.value, end=" ")        # In giá trị của node

# Tạo cây nhị phân như trong ví dụ
#           A
#         /   \
#        B     C
#      /  \
#     D    E
    
root = Node("A")          # Node gốc có giá trị "A"
root.left = Node("B")     # Node con bên trái của gốc có giá trị "B"
root.right = Node("C")    # Node con bên phải của gốc có giá trị "C"
root.left.left = Node("D")# Node con bên trái của "B" có giá trị "D"
root.left.right = Node("E")# Node con bên phải của "B" có giá trị "E"

print("Post-order traversal of the tree:")
post_order_traversal(root)  # Duyệt cây theo thứ tự post-order và in giá trị các node

