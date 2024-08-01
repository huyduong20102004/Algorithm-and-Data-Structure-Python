class Node:
    def __init__(self, data):
        self.head = data
        self.next = None
        self.prev = None
        
class Linkedlist:
    def __init__(self):
        self.head = None 
    def search (self, target):
        current = self.head 
        while current:
            if current.head == target:
                return target 
            else:
                current = current.next
                return None 

    def insert (self, node):
        node.next = self.head 
        if self.head:
            self.head.prev = node 
            self.head = node 
            node.prev = None

    def delete(self, node):
        if node.prev is not None:
            node.prev = node.next 
        else:
            self.head = node.next 
        if node.next is not None:
            node.next.prev = node.prev 

# Tạo các đối tượng Node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Tạo một đối tượng Linkedlist
linked_list = Linkedlist()

# Thêm các node vào danh sách liên kết
linked_list.insert(node1)
linked_list.insert(node2)
linked_list.insert(node3)


# Tìm kiếm một giá trị trong danh sách liên kết
target = linked_list.search(20)
if target is not None:
    print("Giá trị được tìm thấy: ", target)
else:
    print("Giá trị không có trong danh sách.")

# Xóa một node khỏi danh sách liên kết
linked_list.delete(node2)

# In ra danh sách liên kết sau khi xóa
current = linked_list.head
while current:
    print(current.head)
    current = current.next  



