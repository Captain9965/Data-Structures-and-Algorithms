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
4. Each node can have except root, can have at most `n` children and at least `n/2` children.
5. All leaves have the same depth..h-height of the tree.
6. The root has at least 2 children and contains a minimum of 1 key. 
7. If `n>=1`, then for any n-key, B-tree of height h and minimum degree `t>=2`, `h >= logt(n + 1)/2`

## Operations on a B-Tree:

### Searching an element in a B-Tree:

1. Starting from the root of the tree, 