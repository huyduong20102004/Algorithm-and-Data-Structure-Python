import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost (estimated cost to goal)
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    # Initialize start and end nodes
    start_node = Node(start)
    end_node = Node(end)
    
    # Initialize both open and closed lists
    open_list = []
    closed_list = []
    
    # Add the start node to the open list
    heapq.heappush(open_list, start_node)
    
    while open_list:
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)
        
        # If we reached the end node, return the path
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        # Generate neighbors
        neighbors = [
            (0, 1),  # Right
            (0, -1), # Left
            (1, 0),  # Down
            (-1, 0)  # Up
        ]
        
        for direction in neighbors:
            node_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])
            
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])) and grid[node_position[0]][node_position[1]] != 1:
                neighbor_node = Node(node_position, current_node)
                
                if neighbor_node in closed_list:
                    continue
                
                # Calculate costs
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = abs(neighbor_node.position[0] - end_node.position[0]) + abs(neighbor_node.position[1] - end_node.position[1])
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                
                # Check if the neighbor is in the open list
                if add_to_open(open_list, neighbor_node):
                    heapq.heappush(open_list, neighbor_node)
    
    return None  # No path found

def add_to_open(open_list, neighbor_node):
    for node in open_list:
        if neighbor_node.position == node.position and neighbor_node.g > node.g:
            return False
    return True

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)
path = astar(grid, start, end)

print("Path found:", path)
