""" dijkstra's algorithm in python using Prim's algorithm in O(V2): """

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from source")
        for node in range(self.V):
            print(node, "\t", dist[node])


    """ function to find the vertex with the minimum  distance value from 
    the set of vertices not included in the shortest path tree:"""
    def minDistance(self, dist, sptSet):
        """ initialize min distance for next node:"""
        min = sys.maxsize

        """ search the nearest vertex not in spt:"""
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                minIndex = u
        
        return minIndex

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0

        sptSet = [False] * self.V

        for cout in range(self.V):
            """pick the minimum distance vertex from the set of 
            vertices not yet processed. always equal to src in the first iteration: """
            x = self.minDistance(dist, sptSet)


            """ put the min distance vertex in spt:"""
            sptSet[x] = True

            """ update the distance value of the adjacent vertices of the 
            picked vertex only if the current distance is greater than new distance and 
            the vertex is not in spt"""

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    g.dijkstra(0)