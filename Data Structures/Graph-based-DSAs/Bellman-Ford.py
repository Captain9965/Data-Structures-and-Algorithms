""" Bellman Ford's algorithm implementation in python to find shortest path:"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    def print_solution(self, dist):
        print("Vertex\t\tdistance from source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def Bellman_ford(self, src):
        # Step 1: fill in the distance array and predecessor array:
        dist = [float("Inf")] * self.V
        #mark the source vertex:
        dist[src] = 0

        # Step 2: Relax edges |V| - 1 times:
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        #Step 3: detect negative cycle:
        # If value changes, then we have a negative cycle in the graph
        # and we cannot find the shortest distances:
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle!")
                return
        #No negative weight cycle hence print distance and predecessor array:
        self.print_solution(dist)

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    g.Bellman_ford(0)
