class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Hàm tìm giá trị nhỏ nhất trong cây con bên phải
def minValueNode(node):
    current = node

    # Di chuyển đến nút lá bên trái
    while current.left is not None:
        current = current.left
    
    return current

# Hàm xóa một phần tử trong BST
def deleteNode(root, key):
    # Nếu cây rỗng
    if root is None:
        return root
    
    # Nếu giá trị cần xóa nhỏ hơn giá trị của gốc
    if key < root.val:
        root.left = deleteNode(root.left, key)
    # Nếu giá trị cần xóa lớn hơn giá trị của gốc
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    # Nếu tìm thấy nút cần xóa
    else:
        # Nút chỉ có một con hoặc không có con
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # Nút có hai con, tìm nút nhỏ nhất ở cây con bên phải
        temp = minValueNode(root.right)

        # Thay thế giá trị của nút cần xóa bằng giá trị của nút nhỏ nhất
        root.val = temp.val

        # Xóa nút nhỏ nhất trong cây con bên phải
        root.right = deleteNode(root.right, temp.val)
    
    return root

# Hàm duyệt Inorder để kiểm tra cây
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Khởi tạo cây và chèn các phần tử để kiểm tra thao tác xóa
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)

print("Inorder traversal trước khi xóa:")
inorder(root)  

# Thực hiện xóa phần tử 20
root = deleteNode(root, 20)

print("\nInorder traversal sau khi xóa 20:")
inorder(root) 


