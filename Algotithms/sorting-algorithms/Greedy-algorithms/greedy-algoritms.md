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