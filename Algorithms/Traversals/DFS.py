# Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking
# Steps:
# 1. Choose starting node and maintain a visited array
# 2. Mark current node as visited -> for each adjacent nodes: recursively call DFS
# 3. Continue until all reachable nodes are visited
# Time complexity: O(V+E)
# Space complexity: O(V+E)


def dfs_rec(adj, visited, s):
    # Mark the current vertex as visited
    visited[s] = True

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_rec(adj, visited, s)

def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)


# Examples  
V = 5

# Create an adjacency list for the graph
adj = [[] for _ in range(V)]

# Define the edges of the graph
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

# Populate the adjacency list with edges
for e in edges:
    add_edge(adj, e[0], e[1])

source = 1
print("DFS from source:", source)
dfs(adj, source)