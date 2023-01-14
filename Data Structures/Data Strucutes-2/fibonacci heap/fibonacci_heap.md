# Fibonacci Heap:

This is a data structure that consists of a collection of trees which follow a min heap or max heap property.

Here, a node can have 2 children or no children at all.
It has more efficient heap operations than binomial or binary heaps.

It is called **fibonacci** because the trees are constructed in a way such that the tree of order `n`  has at least `Fn+2` nodes in it , where `F(n + 2)` is the `(n + 2)th` Fibonacci number.

## Properties of a Fibonacci Heap:
1. It is a set of min-heap ordered trees.( the parent is always smaller than the children)
2. A pointer is maintained at the minimum element node.
3. It consists of a set of marked nodes( decrease key operation).
4. The trees with in a Fibonacci heap are unordered but rooted.
## Memory representation of  the Nodes in a Fibonacci Heap:

- The roots of all the trees are linked together for faster access.
- The child nodes of a parent node are connected to each other through a circular doubly linked list.

Advantages of using a circular doubly linked list:
1. Deleting a node from the tree takes `0(n)` time.
2. The concatenation of 2 such lists takes `0(n)` time.

## Operations on a fibonacci Heap:
### Insertion:
1. Creat a new node for the element.
2. Check if the heap is empty.
3. If heap is empty, set the new node as a root node and mark it as `min`
4. Else, insert the node into the root list and update `min`

### Find min:
The minium element is always given by the `min` pointer.

### Union:
The Union of 2 fibonacci heaps consists of the following steps:
1. Concantenate the roots of both heaps.
2. Update `min` by selecting the minimum key from the new root list.

### Extract Min:

This is the most important operation in a fibonacci heap during which the node with the minimum value is removed from the heap and the tree is readjusted.

Steps:
1. Delete the min node.
2. Set the min pointer to the next root in the root list.
3. Create an array of size equal to the maximum degree of the trees in the heap before deletion.
4. Repeat the steps 5 - 7 until there are no multiple roots with the same degree.
5. Map the degree of the current root( min pointer ) to the degree in the array.
6. Map the degree of the next root to the degree in array.
7. If there are more than two mappings with the same degree, appy the union operation to those roots such that the min-heap property is maintained.i.e (the minimum is at the root.)

### Decreasing a key:

The value of a key is decreased to a lower value. The following functions are used for this: 

### Decrease key:
1. Select the node to be decreased `x` and change it to new value `k`
2. If the parent of `x`, `y` is not `NULL`, and the key of that parent is greater than `k`, then call `Cut(x)`  and `Cascading-Cut(y)` subsequently.
3. If the key of `x` is smaller than that of `min`, then mark `x` as min.

### Cut:
1. Remove `x` from the current position and add it to the root list.
2. If `x` is marked, then mark it as false.

### Cascading-Cut(y):
1. If the parent of `y` is not `null`, then:
2. If `y` is unmarked, then mark `y`.
3. Else, call `Cut(y)` and Cascading-Cut(parent of y)`

### Deleting a node:
1. Let `k` be the node to be deleted.
2. Apply decrease-key operation to decrease the key to its lowest possible value.(i.e - infinity)
3. Apply extract-min to remove this key

### Complexity:
Decrease key: 0(1)
Delete node: 0(log n)
