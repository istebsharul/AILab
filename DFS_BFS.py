from collections import deque

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Breadth-First Search (BFS)
def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            neighbors = graph[vertex]
            for neighbor in neighbors:
                queue.append(neighbor)

# Depth-First Search (DFS)
def dfs(start):
    visited = set()

    def dfs_recursive(vertex):
        nonlocal visited
        visited.add(vertex)
        print(vertex, end=' ')
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)

# Example usage
print("BFS Traversal:")
bfs('A')
print("\nDFS Traversal:")
dfs('A')
