from collections import deque

def bfs(graph, start):
    visited = set()  # Khởi tạo tập hợp các đỉnh đã được duyệt
    queue = deque([start])  # Khởi tạo hàng đợi với đỉnh khởi đầu

    while queue:  # Duyệt hàng đợi cho đến khi nó trống
        vertex = queue.popleft()  # Lấy đỉnh đầu tiên trong hàng đợi
        if vertex not in visited:  # Nếu đỉnh chưa được duyệt
            print(vertex, end=" ")  # In đỉnh ra màn hình
            visited.add(vertex)  # Đánh dấu đỉnh là đã duyệt

            for neighbor in graph[vertex]:  # Duyệt qua tất cả các đỉnh kề với đỉnh hiện tại
                if neighbor not in visited:  # Nếu đỉnh kề chưa được duyệt
                    queue.append(neighbor)  # Thêm đỉnh kề vào hàng đợi để duyệt sau này

# Đồ thị biểu diễn dưới dạng danh sách kề
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("BFS traversal:")
bfs(graph, 'A')  # Bắt đầu duyệt từ đỉnh 'A'
