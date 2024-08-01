class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Hàm chèn một phần tử vào BST
def insert(root, key):
    # Nếu cây rỗng, trả về một nút mới
    if root is None:
        return Node(key)
    
    # Nếu giá trị nhỏ hơn gốc, chèn vào cây con bên trái
    if key < root.val:
        root.left = insert(root.left, key)
    # Nếu giá trị lớn hơn gốc, chèn vào cây con bên phải
    elif key > root.val:
        root.right = insert(root.right, key)
    
    # Trả về gốc của cây đã được cập nhật
    return root

# Hàm duyệt Inorder để kiểm tra cây
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Sử dụng các hàm
root = None
keys = [20, 10, 30, 5, 15, 25, 35]

for key in keys:
    root = insert(root, key)

print("Inorder traversal sau khi chèn các phần tử:")
inorder(root)  
