# GRAPH BASED DSA's:
This is a collection of nodes that are connected to one another and have data. Every relationship is an edge from one node to another. In a social media application, everything is a node. Every post, every like, photo etc. Every relationship is an edge. And an edge is created for every new node's relationship. 

A graph data structure is a data structure that consists of:

1. A collection of vertices: V
2. A collection of edges E, represented as ordered pairs of vertices: {u, v}

### Graph Terminologies:
***
**Adjacency** - A vertex is said to be adjacent to another vertex if if there is an edge between them. 

**Path** - A sequence of edges that allows one to move from one vertex to another. 

**Directed Graphs** - The edges in such a graph are represented as arrows to show th direction of the edge.

### Graph representation:
***
This is a 2D array of V x V vertices. Each row and column represent a vertex. If the value of any element `a[i][j]` is 1, it represents that there is an edge connecting vertex i and vertex j. 
In an undirected graph, the adjacency matrix is symmetrical about the diagonal.
Edge lookup is extremely fast( checking whether an edge exist between 2 nodes ) but we have to reserve a lot of space to cater of every possible link between all the vertices.

### Adjacency List:
***
It represents a graph as an array of linked lists.

The index of an array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex. 

Is efficient in terms of storage because we only need to store the values for the edges.

In an **undirected graph**, the edges do not point in any direction, they are bidirectional.
On the other hand, in a **connected graph**, there ies always a path from one vertex to any other vertex.

## Spanning Tree:
This is a sub-graph of an undirected connected graph which includes all the vertices of the graph with a minimum number of edges. 

The total number of spanning trees that can be created from a graph with vertices `n` is `n^(n-2)`
### Minimum spaning tree:
In this spanning tree, the sum of the weight of the edges is as minimum as possible.

### Spanning tree applications:
1. Computer network routing protocol.
2. Cluster analysis.
3. Civil network planning.

For *minimum spanning trees*:

1. To find paths in the map.
2. To design telecommunication networks, water networks, and eletrical grids.

### Strongly connected components:

This refers to the portion of a connected graph where there is a path from each vertex to anothe vertex. 

These components can be found using **Korasaju's** algorithm.

### Korasaju's algorithm:
This is based on depth first search algorithm implemented twice. 

Steps involved:
1. Perform a depth first search on the whole graph. Starting from vertex-0, visit all the child vertices and mark the visited vertices as done. If a vertex leads to an already visited vertex, push this vertex onto the stack.
2. Go to the previous vertice and visit all its children sequentially. Push the end vertex onto the stack.
3. Go to the previous vertice and visit all its children. If all its children have been visited already, then push it onto the stack.
4. Reverse the original graph.
5. Perform a depth first search on the reversed graph. 
    - Start form the top of the stack.
    - Traverse through all of its child vertices. Once the visited vertex is reached, a strongly connected component is formed.

### Korasaju's algorithm complexity:
It runs in linear time .i.e `0(V + E)`

### Applications of strongly connected components:
1. vehicle routing applications
2. Maps
3. Model checking in formal verification.


## Adjacency Matrix:
This is a way of representing a graph as a matrix of booleans, with the boolean value indicating whether there is a direct path between 2 vertices.


Each cell in the matrix is represented as `Aij` where `i` and `j` are the vertices. 

In the case of undirected graphs, the matrix is symmetrical about the diagonal because of every edge (i, j), there is also an edge (j, i).

### Pros of an adjacency matrix:
1. the basic operations such as checking whether there is an edge from one vertex to another, removing and adding an edge are extremely time efficient, constant time operations.

2. If the graph is dense and there is a large number of edges, an adjacency matrix should be the first choice. Even if it is sparse, we can represent it using data structures for sparse matrices.

3. The use of matrices lends itself to recent hardware accelerations especially in GPUs.

4. Performing operations on an adjacency matrix can give many insights on the nature of the graph and the relationships between the vertices.

### Cons of an adjacency matrix:

1. The `V * V` space requirement makes it a memory hog. Graphs out in the wild usually do not have too many connections and this is why adjacency lists are preferred for most tasks.
2. While basic operations are easy, others like `inEdges` and `outEdges` are 

### Applications of an adjacency matrix:
1. Creating routing tables in networks.
2. Navigation tasks.

## Adjacency List:
A graph is represented as an array of linked lists with each index of the array representing a vertex and each linked list represents other vertices which have an edge with the vertex.

### Pros:
1. Efficient in terms of storage because we only need to store values for the edges.
2. Also helps to find the vertices that are adjacent to a vertex easily. 

### Cons:
1. Finding the adjacent list is not quicker than the adjacent matrix because all connected nodes must first be explored to find them.

### Adjacency List structure:

The simplest implementation needs a node structure to store a vertex and a graph data structure to organize the nodes.

To stay close to the basic definition of a graph(a collection of edges and vertices), we use an unlabelled graph as opposed to an unlabelled one. ie. vertices are identified by the indices 0, 1, 2..

## Applications of an Adjacent List:
1. It is faster to use an adjacent list for graphs having less number of edges

## Depth first search:

This is a recusive algorithm for traversing all the vertices of a tree or graph data structure.

Each vertex is categorized as visited or not visited.The purpose of the algorithm is to mark vertices as visited while avoiding cycles.

Working:
1. Start by putting any of the vertices on top of a stack.
2. Take the item on top of the stack and mark it as visited.
3. Create a list of that vertex's adjacent nodes.Add the ones that aren't visited to the top of the stack
4. Keep repeating until the stack is empty.

## Complexity of DFS algorithm:
Time complexity is `0(V + E)`
Space complexity is `0(V)`

## Application of DFS:
1. For finding the path.
2. to test whether a graph is bipartite.
3. finding strongly connected components in graphs.
4. detecting cycles in graphs



## Breadth first Search(BFS):

1. Start by putting any one of the graph's vertices at the back of a queue.
2. Take the front item of the queue and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones that are not visited to back of the queue.
4. Keep repeating this until the queue is empty.



## Bellman Ford's Algorithm:

Helps us find the shortest path from a vertex to all other vertices of a weighted graph.

Similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.


### why negative weights:

They may be used to represent phenomena like cashflow, heat loss/absorption etc. 
We have to be careful with negative weight edges because they can introduce negative weight cycles i.e. a cycle that will reduce the total path distance by coming back to the same point.

shortest path algorithms like Dijkstra's algorithm are unable to detect such a cycle and can give an incorrect result because they can go through a negative weight cycle and reduce the path length.

## Working of Bellman Ford's algorithm:

It starts by overestimating the length of the path from one vertex to all other vertices. It then interatively relaxes those estimates by finding shorter paths than the previously overestimated paths. 

By doing this for all the vertices, we can guarantee that the result is optimized.

### Bellman Ford's pseudocode:

We need to maintain the distance of every vertex. We can store that in any array of size `V`.

We want to know the length of the shortes path and the shortest path as well. For this, we map each vertex to the vertex that last updated its path.

Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.


## Bellman Ford's complexity:
Time complexity:

Best case complexity -> `O(E)`
Average and worst case complexity -> `O(VE)`

Space complexity:

Space complexity -> `O(V)`

## Applications:

1. Calculating shortest paths in routing algorithm.
2. for finding the shortest path.


