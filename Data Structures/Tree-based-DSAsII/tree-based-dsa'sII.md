# B-Tree:
This is a self balancing tree in which each node can contain more than one key and have more than two children. It is a generalized form of a binary search tree.

Also called a **height balanced m-way tree**

## Need for the B-Tree:
This came with the need for faster access times for data in physical storage media like hard disks.
This is due to the reduction in tree height and hence reduced access times for data.

## Properties of a B-Tree:
1. For each node, `x`, the keys are stored in increasing order.
2. In each node, there is a boolean value, `x.leaf` that is true when `x` is a leaf.
3. If `n` is the order of the tree, each internal node can contain at most `n-1` keys along with a pointer to each child.
4. Each node, except root, can have at most `n` children and at least `n/2` children.
5. All leaves have the same depth..h-height of the tree.
6. The root has at least 2 children and contains a minimum of 1 key. 
7. If `n>=1`, then for any n-key, B-tree of height h and minimum degree `t>=2`, `h >= logt(n + 1)/2`

## Operations on a B-Tree:

### Searching an element in a B-Tree:

1. Starting from the root of the tree, compare k with the first key of the node. If `k= the first key of the node`, then return the `node` and the `index`. 

2. If `k.leaf = true` then return `NULL`
3. If `k < the first key of the root node` then search the left child of this key recursively
4. If there is more than one key in the node, and `k > the first key in the node`, compare `k` with the next key in the node. If `k < next key`, then search the left child of this key. Else search the right child of this key. 
5. Repeat until the leaf is reached.

### Insertion in a B-Tree:

This happens in 2 steps..one is searching the appropriate node to insert the element and then splitting the node if required. The approach in this is `bottom up`.

Steps:
1. If tree is empty, allocate a root node and insert the key.
2. Update the allowed number of keys in the node. 
3. Search the appropriate node for insertion.
4. If the node is full:
    - insert the elements in an increasing order
    - now there are elements greater than its limits, so split at the median.
    - push the median key upwards and make the left keys as a left child and the right keys as a right child.
5. If the node is not full:
    - insert the node in increasing order. 
