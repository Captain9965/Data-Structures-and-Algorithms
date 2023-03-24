""" Ford Fulkerson algorithm in python:"""



class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    """ using BFS as a searching algorithm:"""
    def bfsSearch(self, s, t, parent):
        visited = [False] * self.ROW
        queue = []

        #append source: 
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
    
    def FordFulkerson(self, source, sink):
        parent = [-1] * self.ROW
        maxFlow = 0

        while self.bfsSearch(source, sink, parent):
            print(parent)
            pathFlow = float("inf")
            s = sink
            while(s != source):
                pathFlow = min(pathFlow, self.graph[parent[s]][s])
                s = parent[s]
            """ adding the path flows:"""
            maxFlow += pathFlow

            """ updating the residual values of the edges:"""
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= pathFlow
                self.graph[v][u] += pathFlow
                v = parent[v]
        return maxFlow

if __name__ == "__main__":
    graph = [[0, 8, 0, 0, 3, 0],
            [0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 7, 2],
            [0, 0, 0, 0, 0, 5],
            [0, 0, 7, 4, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    g = Graph(graph)

    source = 0
    sink = 5

    print("Max flow %d " % g.FordFulkerson(source, sink))