

# Dynamic Programming:
This is a technique used in computer programming that helps to efficiently solve a class of problems that have overlapping subproblems and optimal substructure property.

If a problem can be divided into subproblems and which in turn can be divided into more subproblems, and if there is overlapping among these subproblems then the solutions to these subproblems can be saved for future reference. In this way, the efficiency of the CPU can be enhanced.

such problems involve repeatedly calculating the value of same subproblems to find an optimal solution.

## Example: 
## The Fibonacci series: 
Given by:
```
Let n be the number of terms.

1. If n <= 1, return 1.
2. Else, return the sum of two preceding numbers.
```
## How it works:

It involves storing the results of subproblems, such that when they are needed, they are at hand and they need not be calculated again.

This technique is called memoization and it is a top down approach:
```
var m = map(0 → 0, 1 → 1)
function fib(n)
    if key n is not in map m 
        m[n] = fib(n − 1) + fib(n − 2)
    return m[n]
```
By reversing the algorithm and working from the base case, we can implement dynamic programming in a bottom-up manner. 

Example:
```
function fib(n)
    if n = 0
        return 0
    else
        var prevFib = 0, currFib = 1
        repeat n − 1 times
            var newFib = prevFib + currFib
            prevFib = currFib
            currFib  = newFib
    return currentFib
```
In an algorithm like Merge Sort , the reason why dynamic programming cannot be used is that there are no overlapping subproblems like in the fibonacci sequence. In such a case, we can only reach a solution through a divide and conquer approach.

Greedy algorithms are also an optimization tool but greedy algorithms attempt to find locally optimum solutions which may not be optimum down the road. dynamic programming on the other hand, attempts to find the optimal solutions to sub-problems and then makes an informed choice to combine the results of those sub-problems to find the most optimum solution

Examples of these dynamic algorithms:

# Floyd Warshall algorithm:
This is an algorithm for finding the shortest path between all pairs of vertices in a weighted graph, both directed and undirected. 

It however doesn't work for graphs with negative cycles( where the sum of edges in a cycle is negative )

## Working:
```
n = no of vertices
A = matrix of dimension n*n
for k = 1 to n
    for i = 1 to n
        for j = 1 to n
            Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
return A
```
Note that in every iteration, the previous matrix is used to generate the new matrix. and the `kth` row and column remain the same.

## Complexity:
Since there are 3 loops, time complexity is `O(n3)`

Space complexity is `O(n2)`

## Applications:
1. To find the shortest path in a directed graph.
2. To find the transitive closure in a directed graph.
3. To find the inversion of real matrices.
4. Testing whether a directed graph is bipartite. 