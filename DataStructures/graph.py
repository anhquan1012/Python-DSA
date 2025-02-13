# Graph is data structure which contain vertices, which are connected to each other through edges
# Graphs are divided into 3 categories: cyclic/acyclic, weighted/unweighted, directed/undirected
# A graph can be represented in 3 ways: adjacency list, adjacency matrix, edge list.
# Here is the implementation of undirected graph using adjacency list

#%%
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()
    
    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)


class Graph:
    vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


#%%
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'BC', 'EF', 'EH', 'DK']
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print_graph()
