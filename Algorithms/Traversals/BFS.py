# Breadth First Search (BFS) is a fundamental graph traversal algorithm. It begins with a node, then first traverses all its adjacent. Once all adjacent are visited, then their adjacent are traversed.
# Steps:
# 1. Create a FIFO queue and enqueue the starting node. Maintain a visited array
# 2. While queue is not empty: dequeue a node -> enqueu all unvisited adjacent nodes -> mark as visited
# 3. Repeat step 2 until the queue is empty
# Time complexity: O(V+E)
# Space compleity: O(V)


from collections import deque


def bfs(adj, s):
    # Init a queue to visit
    q = deque()
    # Initially mark all the vertices as not visited
    # When we push a vertex into the q, we mark it as 
    # visited
    visited = [False] * len(adj)

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


# Examples
# Number of vertices in the graph
V = 5

# Adjacency list representation of the graph
adj = [[] for _ in range(V)]

# Add edges to the graph
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 1, 4)
add_edge(adj, 2, 4)

bfs(adj, 0)