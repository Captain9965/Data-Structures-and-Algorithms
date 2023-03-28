# Greedy algorithms:
This is an approach for problem solving by selecting the best option available at the moment. It doesn't worry that it may be sub-optimal.

It doesnt reverse the earlier decision, even if the choice is wrong, it works in a top down approach.

We can determine whether the algorithm can be used with a problem if the problem had the following properties:


## 1. Greedy choice property:

If an optimal solution to the problem can be found by choosing the best choice at each step without reconsidering the pervious step once chosen, then the problem can be solved using the greedy approach. This is the `greedy choice property`.

## 2. Optimal substructure:
If the optimal solution to the problem corresponds to the optimal solution to the sub-problems, then the problem can be solved using the greedy approach.

## Advantages of Greedy approach:
1. The algorithm is easier to describe.
2. Better perfomance compared to other algorithms, but not in all cases.

## Drawbacks:
It doesnt always produce the optimal solution.

## Working:
1. To begin with, the solution set is empty.
2. At each step, an item is added onto the solution set until a solution is reached.

# Ford Fulkerson algorithm:

This is a greeedy approach for calculating the maximum possible flow in a network or graph.

The term `flow network` is used to describe a network of vertices and and edges with a source and a sink. Each vertex, except `S` and `T` can receive and send and equal amount of stuf through it. `S` can only send and `T` can only receive.

## Terminologies used:
___
 ## Augmenting path:
 This is the path available in a flow network

 ## Residual graph:
 The flow network that has additional possible flow

 ## Residual capacity:
 Capacity of the edge after subtracting the flow from the maximum capacity.

 ## Working
 ---
 1. Initialize flow in all the edges to 0
 2. While there is an augmenting path between a source and a sink, add this path to the flow.
 3. Update the residual graph.

 We can also consider reverse path if required because if we do not, we may never find maximum flow.

 Note that if the capacity for any edge is full, then that path cannot be used.

 ## Applications:
 1. Water distribution pipeline.
 2. Bipartite matching problem.
 3. Circulation with demand

 # Dijkstra's algorithm:
This allows us to find the shortest path between any 2 vertices in a graph.
Differs from the min spanning tree because this may not include all the vertices in the graph.

## Working:
It works on the basis that any subpath `B->D`of the shortest path `A->D`is also the shortest path between the vertices `B` and `D`.
Djikstra used this property in the opposite direction.i.e. we overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbours to find the shortest subpath to those neighbours.
Uses the greedy approach since we find the next best approach hoping that the end result is the best solution for the problem.

## Pseudocode:
To maintain the path distance between the vertices, we use an array of size `v` where `v` is the number of vertices.
to know the shortest path, we need to map each vertex to the vertex that last updated its path length. 

Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.

A min priority queue can be used to efficiently receive the vertex with the least path distance.

```
function dijkstra(G, S)
    for each vertex V in G
        distance[V] <- infinite
        previous[V] <- NULL
        If V != S, add V to Priority Queue Q
    distance[S] <- 0
	
    while Q IS NOT EMPTY
        U <- Extract MIN from Q
        for each unvisited neighbour V of U
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]
                distance[V] <- tempDistance
                previous[V] <- U
    return distance[], previous[]
```
## Complexity:
```
- Time complexity is O(E log V) where E is the number of edges and V the number of vertices.

- Space complexity is O(V)
```

## Application:
1. Finding the shortest path.
2. Social networking applications.
3. In a telephone network.
4. Finding locations in a map.

# Kruskal's Minimum spanning tree algorithm:

## What is a spanning tree?
It is a subset of a connected graph G where all edges are connected i.e. one can traverse to any edge from a paritcular edge with or without intermediaries. It must not have any cycle in it. If there are N vertices in a connected graph, then the number of edges that a connected graph may have is N - 1. 

## What is a minumum spanning tree?
A minumum weight spanning tree for a connected, weighted or undirected graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree. 

## Working of Kruskal's:
1. sort all edges from low weight to high weight.
2. Take the edge with the lowest weight and add it to the spanning tree.If adding the edge created a cycle, then reject this edge. 
3. Keep adding edges until we reach all vertices.

## Kruskal's complexity:
Time complexity is `O(E log E)`

## Applications:
1. Laying out electrical wiring.
2. computer networks, LAN. 

# Prim's algorithm:
It always starts with a single node and it moves through several adjacent nodes in order to explore all the connected edges along the way

It starts with an empty spanning tree. The idea is to maintain 2 sets of vertices. The first contains vertices already included in MST, and the other those not yet included. At every step, it considers all edges that connect the 2 sets and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of the edge to the set containing MST.

## Working:
1. Create a set mstSet that keeps track of vertices already included in MST.
2. Assign a key value to all vertices in the input graph. Assign a value of INF to all key values. Assign a key value of 0 to the first vertex so that it is picked first.
3. While mst doesnt include all vertices:
    - Pick a vertex  u which is not there in mstSet and has a minimum key value.
    - include u in the mstSet.
    - Update the key values of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.for every adjacent vertex v, if the weight of u-v is less than the previous key value of v, update the key value as the weight of u-v 

## Pseudocode:
```
PrimMST(graph G)
	for each vertex v in G:
		v.distance = infinity
	start = arbitrary vertex
	start.distance = 0
	priorityQueue = all vertices in G
	while priorityQueue is not empty:
		u = vertex with smallest distance in priorityQueue
		remove u from priorityQueue
		for each neighbor v of u:
			if v is in priorityQueue and weight(u, v) < v.distance:
				v.distance = weight(u, v)
				v.parent = u
	return MST
```
## Complexity:
Time complexity is `O(V2)` for an adjacency matrix implementation and `O(E log V)` for an binary heap and adjacency list implementation.

Space complexity is `O(V)`

# Huffman Coding:
This is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters with the length of the assigned codes being based on the frequencies of corresponding characters.

The variable length codes assigned to input characters are prefix codes and are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. 

Steps in Huffman coding:
1. Building a Huffman tree from input characters.
2. Traverse the Huffman tree and assign codes to the characters.

## Building a Huffman tree:
Input is an array of unique characters along with their frequency of occurrences and output is the Huffman Tree. 

1. Create a leaf node for each unique character and build a minheap of all leaf nodes( min heap here is used as a priority queue). The value of the frequency field is used to compare 2 nodes min heap. Initially, the least frequent character is at the root.

2. Extract 2 nodes with the minumum frequency from the heap. 
3. Create a new internal node with a frequency equal to the sum of the 2 node frequencies. Make the first extracted node as its left child and the other its right child. Add this node to the minheap.
4. Repeat steps 2 and 3 until the heap contains only one node. The remaining node is the root node and the tree is complete. 

## Printing the codes:
1. Traverse the tree formed, starting from the root. Maintain an auxiliary array. If we move to the left child, write 0 to the array. While moving to the right child, write 1 to the array.
2. Print the array when a leaf node is encountered. 

## Huffman coding complexity:
Time complexity is `0(n log n)`
Extracting minimum frequency from the queue takes place `2 *(n - 1)` times and its complexity is `0 (log n)`

## Huffman coding applications:
1. Used in conventional compression formats like GZIP, BZIP, PKZIP, 
2.  Text and data transmission. 