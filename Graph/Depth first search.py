def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Khởi tạo tập hợp các đỉnh đã được duyệt
    visited.add(start)  # Đánh dấu đỉnh hiện tại là đã duyệt
    print(start, end=" ")  # In đỉnh hiện tại ra màn hình

    for neighbor in graph[start]:  # Duyệt qua tất cả các đỉnh kề với đỉnh hiện tại
        if neighbor not in visited:  # Nếu đỉnh kề chưa được duyệt
            dfs(graph, neighbor, visited)  # Tiến hành duyệt đỉnh kề đó

# Đồ thị biểu diễn dưới dạng danh sách kề
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS traversal:")
dfs(graph, 'A')  # Bắt đầu duyệt từ đỉnh 'A'

