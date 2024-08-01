class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.data = []
    def push(self, node):
        self.data.append(node)
    def pop(self):
        self.data.pop()



# Tạo một đối tượng Stack
stack = Stack()

# Thêm các node vào Stack
node1 = Node(10)
stack.push(node1)

node2 = Node(20)
stack.push(node2)

node3 = Node(30)
stack.push(node3)

# Hiển thị Stack ban đầu
print("Stack ban đầu:")
print(stack.data)

# Xóa node cuối cùng khỏi Stack
stack.pop()

# Hiển thị Stack sau khi xóa
print("Stack sau khi xóa:")
print(stack.data)