# Định nghĩa một lớp đại diện cho một nút trong cây
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Hàm để duyệt cây theo thứ tự In-order và in ra giá trị của các nút
def inorder_traversal(node):
    if node is not None:
        # Duyệt cây con bên trái
        inorder_traversal(node.left)
        # In ra giá trị của nút hiện tại
        print(node.value, end=" ")
        # Duyệt cây con bên phải
        inorder_traversal(node.right)

# Tạo một cây như trong ví dụ
'''
       A
      / \
     B   C
    / \
   D   E
'''
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

print("In-order traversal of the tree:")
inorder_traversal(root)
