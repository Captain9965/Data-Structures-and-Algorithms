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

