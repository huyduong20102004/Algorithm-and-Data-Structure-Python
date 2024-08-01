class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be null.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    
    def delete(self, node):
        if node is None or self.head is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Tạo một đối tượng DoublyLinkedList
dll = DoublyLinkedList()

# Thêm các node vào danh sách liên kết đôi
dll.insert_front(10)
dll.insert_front(20)
dll.insert_front(30)

# In ra danh sách liên kết đôi
print("Danh sách liên kết đôi ban đầu:")
dll.display()

# Tìm kiếm một giá trị trong danh sách liên kết đôi
target_node = dll.search(20)
if target_node:
    print("Giá trị được tìm thấy: ", target_node.data)
else:
    print("Giá trị không có trong danh sách.")

# Xóa một node khỏi danh sách liên kết đôi
dll.delete(target_node)

# In ra danh sách liên kết đôi sau khi xóa
print("Danh sách liên kết đôi sau khi xóa node có giá trị 20:")
dll.display()