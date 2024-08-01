from collections import deque

class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, node):
        self.data.append(node)

    def dequeue(self):
        self.data.popleft()

    def count_nodes(self):
        return len(self.data)
    





    

# Tạo một đối tượng Queue
queue = Queue()

# Thêm các node vào hàng đợi
node1 = Node(10)
queue.enqueue(node1)

node2 = Node(20)
queue.enqueue(node2)

node3 = Node(30)
queue.enqueue(node3)

# Hiển thị hàng đợi ban đầu
print("Hàng đợi ban đầu:")
print(queue.data)

# In số lượng node trong hàng đợi
print("Số lượng node trong hàng đợi:", queue.count_nodes())

# Xóa node đầu tiên khỏi hàng đợi
queue.dequeue()

# Hiển thị hàng đợi sau khi xóa
print("Hàng đợi sau khi xóa:")
print(queue.data)

# In số lượng node trong hàng đợi sau khi xóa
print("Số lượng node trong hàng đợi sau khi xóa:", queue.count_nodes())