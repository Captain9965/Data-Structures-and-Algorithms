"""Adjacency matrix representation in python:"""

class Graph:
    #initialize the matrix:
    def __init__(self, size):
        self.adjMatrix = []
        self.size = size
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = True
        self.adjMatrix[v2][v1] = True
    
    def remove_edges(self, v1, v2):
        if not self.adjMatrix[v1, v2]:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1, v2] = False
        self.adjMatrix[v2, v1] = False
    def __len__(self):
        return self.size
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{: 4}'.format(val), end=''),
            print("")

    
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()