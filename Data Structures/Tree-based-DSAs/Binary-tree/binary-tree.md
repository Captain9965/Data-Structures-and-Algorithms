# Binary Tree

This is a tree data structure in which each parent node can have at least 2 child nodes.

## Types of a binary tree:

### Full binary tree:

Every parent or internal node has 2 or no children

### Perfect binary tree:

This is a binary tree in which every internal node has exactly 2 child nodes and all the leaf nodes are at the same level.

### Complete binary tree:

Is just like a full binary tree but with 2 major differences:

1. every level must be completely filled
2. All leaf elements must lean towards the left
3. The last leaf element might not have a right sibling i.e. it doesn't have to be a full binary tree.

### Degenerate or pathological tree:

A tree having a single child, either left or right. 

### skewed binary tree:

This is a tree dominated by either left-leaning or right leaning nodes.

### Balanced binary tree:

In this binary tree, the difference between the height of the left and right sub-tree for each node is either 0 or 1

### Binary tree applications:

1. Easy and quick access to data
2. In router algorithms
3. Implementation of heap data structures
4. syntax trees

## Full Binary tree:
In this binary tree, every parent or internal node has either 2 or no children. It is also called a proper binary tree. 

### Full binary tree theorems:

let:
- `i` be the number of internal nodes
- `n` be the total number of nodes
- `l` be the total number of leaves
- `lv` be the number of levels

then:
1. The number of leaves is `i + 1`
2. The total number of nodes is `2i + 1`
3. The number of internal nodes is `(n - 1) / 2`
4. The number of leaves is `(n + 1) / 2`
5. The total number of nodes is `2l -1`
6. The number of internal  nodes is `l - 1`
7. The number of leaves is at most `2^(lv -1)`


## Perfect binary tree:

This is a binary tree in which every internal node has exactly 2 child nodes and all the leaf nodes are at the same level.
All internal nodes have a degree of 2. 

It can be defined recursively as:
1. If a single node has no children, then it is a perfect binary tree of `h = 0`
2. If a node has `h > 0`, then it is a perfect binary tree if both of its sub-trees are of height `h - 1` and are non-overlapping

## Complete Binary tree:

This is a binary tree in which all the levels are completely filled apart from possibly the lowest one, which is filled from the left.

Like a full binary tree with 2 major differences:

1. All the leaf elements must lean towards the left
2. The last leaf element might not have a right sibling

### How a complete binar tree is created:

1. Select the first element of a list to be the root node.
2. Put the second element as the left child and the third element as the right child.
3. Put the next 2 elements as children of the left node of the second level
4. Keep repeating till the last element.

### Relationship between array indexes and the tree elements:

A complete binary tree has an interesting property that we can use to find the children and parents of any node. 
If the index of any element in the array is `i`, then the element in the index `2i + 1` will become the left child and the element in the index `2i + 1` will become the right child. 

Also, the parent of any element at index `i` is given by the lower bound of `(i -1)/2`

### Applications of the tree data structure:
1. Heap sort.
2. Heap based data structures.