# Tree Data Structure

This is a non-linear hierachial data structure that consists of nodes connected by edges.

## why Trees?

In order to perform computations in linear data structures such as stacks, linked lists or queues, the time complexity increases with increase in data size. Trees allow quicker and easier access to data.

## Terminologies:

### Node:

A node is an entity that contains a key or value and pointers to its child nodes.

The last nodes to each path is called the `child nodes` or `leaf nodes` and they do not contain a link/pointer to child nodes.

The node having at least a child node is called an `internal node`

### Edge:

This is the link between any 2 nodes

### Root:

This is the top most of a Tree

### Height of a node:
 This is the number of edges from a node to the deepest leaf.

 ### Depth of a node:

 Number of edges from the root to the node.

 ### Height of a tree:

 This is the height of the root or th depth of the deepest node.

 ### Degree of a node:

 This is the total number of branches of that node

 ### Forest:

 A collection of disjoint trees. Can be created by cutting the root of a tree.

 ## Types of trees
 1. Binary tree
 2. Binary search tree
 3. AVL tree
 4. B-tree  

 ## Tree Applications:

 1. BSTs are used to check whether an element is present in a set or not.
 2. Heap is a kind of tree used in a quick sort
 3. A modern version of a tree called Tries are used to store routing information
 4. Most modern databases use B-trees and T-trees to store data
 5. Compilers use a syntax tree to validate the syntax of written programs
