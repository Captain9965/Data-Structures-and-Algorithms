""" python implementation of kruskal's algorithm to find a 
minimum spanning tree of a given connected, undirected and weighted graph:"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
    """utility function to find a set of an element i 
    using path compression technique: """

    def find(self, parent, i):
        if parent[i] != i:
            """ reassignment of a node's parent to root node as path
            compression requires: """
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    """ a funciton that requires union of 2 sets of x and y (uses union by rank):"""
    def union(self, parent, rank, x, y):
        """ attach smaller rank tree under root of high rank tree (union by Rank):"""
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        #if ranks are the same, then make one as root and increment its rank by one:
        else:
            parent[y] = x
            rank[x] += 1

    """ main function to contruct mst using Kruskal's algorithm: """

    def kruskalMst(self):
        """ This stores the result: """
        result = []
        i = 0
        e = 0

        """ Step 1: sort all edges in ascending order of their weights"""
        self.graph = sorted(self.graph, key=lambda x : x[2])

        parent = []
        rank = []

        """ create v subsets with single elements:"""
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        """ number of edges to be taken is one less than V:"""
        while e < self.V - 1:
            """Step 2: pick the smallest edge and increment the index for the next iteration: """
            u, v, w = self.graph[i]
            i+=1
            x = self.find(parent, u)
            y = self.find(parent, v)
            

            """ if including this edge does not cause a cycle, then include it in the result
            and increment the index of the result for the next edge: """
            if x != y:
                e +=1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            """discard the edge: """

        minimumCost = 0
        print("Edges in the constructed MST: ")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" %(u, v, weight))
        print("minimum spanning tree: ", minimumCost)


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
 

    g.kruskalMst()
