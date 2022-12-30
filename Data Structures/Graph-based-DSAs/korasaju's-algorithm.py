""" Korasaju's algorithm to find strongly connected components:"""

from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.graph = defaultdict(list)
        self.V = vertex

    #add an edge to the graph:
    def add_edge(self, s, d):
        self.graph[s].append(d)
    
    #dfs:
    def dfs(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        print(d, end= '')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)
    
    #transpose the matrix:
    def transpose(self):
        g = Graph(self.v)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j,i)
        return g

    #print strongly connected components:
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                