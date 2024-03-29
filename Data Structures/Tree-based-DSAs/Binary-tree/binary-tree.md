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


## Balanced Binary tree:

This is a binary tree in which the height of the left and the right binary trees of every node differ by not more than 1

Conditions:
1. The difference between the left and the right subtrees of any node is not more than one. 
2. The left subtree is balanced. 
3. The right subtree is balanced. 


### Balanced tree applications:
1. AVL tree
2. Balanced binary search tree

## Binary Search Tree:

This is a data structure that quickly allows us to maintain a sorted list of numbers. Called a binary search tree because:
- Each node has a maximum of 2 children
- It is called a search tree because it can be used to search for a number in `0(log(n))` time. 

Difference with a regular binary tree:
- All nodes of the left subtree are less than the root node.
- All nodes of the right subtree are more than the root node.

2 basic operations that one can perform on a binary search tree:
### Search algorithm:

The search algorithm relies on the fact that each left subtree has values below the root and each right subtree has values above the root. It follows that if a value is below the root, then we should only search the left subtree and vice versa. 

### Inserting algorithm:

We try to maintain the rule of the left subtree being always less than the root. 
We keep going either to the left or right sub-tree depending on the value and when we reach a point left or right subtree is NULL, we put the new node there. 

### Deletion operation:
1. In the first case, if the leaf to be deleted is the leaf node, we simply delete the node from the tree
2. In the second case, if the node to be delted has only one child node, replace that node with its child node and remove the child node from its initial position.
3. In the third case, if the node to be deleted has 2 children, then get the inorder successor of that node, replace the node with the inorder successor then remove the inorder successor from its original position.

### Time complexity:
`0 (log n)`  in search, insertion and deletion in best case and average complexity and `0(n)` in worst case where `n` is the number of nodes in the tree.

### Space complexity:

Space complexity for all operations is `0(n)`

### Applications of a binary search tree:

1. Multilevel indexing in databases.
2. dynamic sorting.
3. managing virtual memory areas in the Unix kernel.


## AVL Tree:

This is a self-balancing BST in which each node maintains extra information called the **balance factor** which is either 0, -1, or +1. 
Name derived from its inventors **Avelson-Velsky and Landis**

### Balance factor:

The balance factor of a node is the difference between the height of the left sub-tree and the right sub-tree of that node.

`BF = HL -HR or HR - HL`

The self balancing is maintained by the balance factor which should be either of the 3 values `0, +1, -1`


### Operations of an AVL tree:

### 1. Rotation:

This is where the positions of the nodes are interchanged

#### Left Rotate:
In this, the arrangement of nodes in the right is transformed into the arrangement on the left node.

#### Right Rotate:
The arrangement of nodes in the left is transformed into the arrangement on the right node.

#### Left-right Rotation:
The arrangements are first shifted to the left and then to the right.

### Right - left Rotation:
The arrangements are first shifted to the right and then to the left.

### Inserting a new node:

Always inserted as a leaf node with a balance factor equal to 0. 
1. Insert the node as a leaf node.
2. Update the balance factor of the nodes after insertion.
3. If nodes are unbalanced, then rebalance the node.
    - If `BF > 1`, then the height of the left sub-tree is greater than the right sub-tree. So do a right rotation or left-right rotation.
    - If `newNodeKey < leftchildkey` do a right rotation
    - Else do a left-right rotation.
    - If the `BF < -1` then do the converse

### Algorithm to delete a node:

After deleting a node, the balance factors do change. Suitable rotations are made in order to rebalance the balance factor. 

1. Locate the `nodeToBeDeleted` through recursion.
2. Cases for deleting a node:
    - If it is the `leafnode`, then just remove it
    - If it has one child, then substitute the contents with that of the child then remove the child
    - If it has 2 children, then find the inorder successor of the `nodeToBeDeleted` which is the minimum value of key in the right sub-tree. 
3. Update the balance factor of the nodes.
4. Rebalance the tree if unbalanced:
    - If the `BF` of `currentnode` > 1,
        -If `BF` of `leftchild` >= 0, do a right rotation
        - Else do left-right rotation
    - If the `BF` of `currentnode < -1`,
        - If the `rightchild` <= 0, then do a left rotation
        - Else do a right-left rotation

## Complexities:

`0( log n )` in insertion, deletion and search..

## AVL Tree Applications:

1. indexing large records in databases
2. searching in large databases













