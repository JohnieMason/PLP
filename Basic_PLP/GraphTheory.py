# Basic Definitions
# Vertical (nodes) & Edges- Rep objects and their relationships.
# Directed vs Undirected graphs - Important or modelling one-way relationships or networks.
# Graphical representations
# Adjacency list vs Matrix
# choose based on the density of the graph and operations you need to perform.
# Core Algorithms:
# Traversal Techniques - Depth-First Search (DFS) and Breadth-First Search (BFS) for exploring graph structure.
# Shortest path and minimum spanning trees:
# Algorithms such as Dijkstra's, Bellman-Ford, Kruskal's and Prim's underpin applications ranging from routing to network design.
# Examples on DFS and BFS

from collections import deque

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbour in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
print("DFS Traversal starting from A:")
dfs(graph, 'A')
print("\n")

# BFS using Queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([n for n in graph[vertex] if n not in visited])
        print()
print("BFS Traversal starting from A:")
bfs(graph, 'A')



# Explanation
# DFS uses recursive calls to explore deeep as possible before backtracking; BFS  uses Queue to explore neighbor level by level.
# Both techniques are fundamental in solving various graph-related problems.
