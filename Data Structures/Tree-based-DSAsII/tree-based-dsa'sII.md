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

### Deletion in a B-Tree:
This consists of 3 main operations:
- Searching the key to be deleted
- Deleting the key
- Balancing the tree if required.

While doing this, a condition called **underflow** may occur. This is whereby a node contains less than the minimum number of keys it should hold..
Note:

**Inorder predecessor** - This is the largest key on the left child of a node.

**Inorder successor** - This is the smallest key on the right child of a node. 

## Deletion operation:

Facts about a tree of degree `m`:
1. A node can have a maximum of `m` children. ie 3
2. A node can have a maximum of `m - 1` keys. ie 2
3. A node should have a minimum of `m/2` children. ie 2
4. A node, except root node, should have a minimum of `[m/2] - 1` keys. 

3 main cases for deletion:
### Case 1:
The key to be deleted lies in the leaf:
If:
1. The key does not violate the min number of keys a node should hold, we just delete the key.
2. The key violates this minimum, then we borrow a key from its immediate neighbouring sibling node from left to right. 
    - First visit the left sibling and borrow a key if it exceeds the minimum number of allowed keys.
    - Else borrow from the immediate right sibling. 
    - If both the keys have a minimum number of keys, then merge the node with either the right or the left sibling..this merging is done through the parent node. 

### Case 2: 
The key to be deleted lies in the internal node:
1. The internal node, which is deleted, is replaced by an inorder predecessor if the left child has more than the minimum number of keys.
2. Or replaced by an inorder successor if the right child has more than the min number of keys.
3. If either has min number of keys, then merge the left and the right children.
4. After merging, if the parent node has less than the min number of keys, then look for siblings as in case 1

### Case 3:
If the target lies in a internal node and the deletion of a key leads to a fewer number of keys than the minimum, then look for the inorder predecessor then the inorder successor...if both contain min keys, then the children should be merged. If the sibling also contains min number of keys, then merge the node with the sibling along with the parent. 

### Deletion complexity:

Best case time complexity: `0 (log n)`
Average and worst case space complexity: `0(n)` 

# B+ Trees:
This is an advanced form of a self-balancing tree in which all values are present at leaf level. It is important to understand multi-level indexing before B+ trees. Multi-level indexing makes accessing data easier and faster. 
## Properties of a B+ trees:
1. All leaves are the same level
2. The root has at least 2 children
3. Each node can have a maximum of `m` children and at least `m/2`
4. Each node can contain a maximum of `m - 1` keys and a minimum of `[m/2] - 1`

## B- Trees vs B+ Trees:
1. The data pointers are present only at the leaf nodes on a B+ Tree while data pointers are present at internal, leaf, root or root nodes on a B-Tree.

2. The leaves are not connected to each other on a B-Tree but are connected on a B+Tree. 

3. Operations on a B+ Tree are faster than those on a B-Tree. 

## Searching on a B+Tree:
Let the order of the B+Tree be `m` and the data to be searched be `k`.

1. Start from the root node and compare `k` with the keys at the root node.
2. If `k < k1`, then go to the left child of the root node.
3. Else if `k == k1`, then compare `k2`. If `k < k2`, then `k` lies between `k1` and `k2`. So search in the left node of `k2`. 
4. If `k` is `> k2` do steps 2 and 3 with `k3..` and so on and so forth. 
5. Repeat the steps until a leaf node is reached. 
6. If `k` exists in the leaf nodes, then return true otherwise return false. 

## Insertion on a B+ Tree:

Inserting an element into a B+Tree involves: searching the appropriate leaf, inserting the element and then balancing/splitting the tree. 

1. Since the element is inserted into the leaf node, go to the appropriate leaf node.

2. Insert the key into the leaf node.

    *Case 1*:
    - If the leaf is not full, insert the key in increasing order

    *Case 1*:
     - If the leaf is not full, insert the key into the leaf node in increasing order and balance the tree in the following way:
     - Break the node in the `m/2`the position.
     - Add the `m/2`th key in the parent node as well.
     - If the parent node is already full, repeat the second and third steps as well. 

## Insertion complexity:
1. Time complexity: `0(t.logt n)`
2. The complexity is dominated by: `0(logt n)`

## Deletion in a B+Tree:

Deleting a key involves searching the node where they key exists and then deleting the key and balancing the key. `Underflow` occurs when there are less number of keys in a node than the minimum number of keys it should hold. 

While deleting a key, we have to take care of the keys present in the internal nodes as well because the values are redundant in a B+Tree 

### Case 1:
The key to be deleted is present only on the leaf node, not on the indexes, there are 2 cases for it.

1. If there is more than minimum number of keys in the node, simply delete the key. 
2. There is an exact miniumum number of keys in the node. Delete the key and borrow a key from the immediate sibling. Add the median key of the sibling node to the parent. 

### Case 2:
The key to be deleted is present in the internal nodes as well. Then we have to remove them from the internal nodes as well. Cases:

1. If there is more than the minimum number of keys in the node, simply delete the key from the leaf and internal node. Fill the empty node with the inorder successor. 

2. If there is an exact minimum number of keys in the node, then delete the key and borrow a key from its immediate sibling(through the parent). Fill the empty space created in the index(internal node) with the borrowed key.

3. Similar to case 2 but here, empty space is generated above the immediate parent node.After deleting the key, merge the empty space with its sibling. Fill the empty space in the grandparent node with the inorder successor. 

### Case 3:

In this case, the height of the tree gets shrinked. This is created by special conditions.


# Red-black Tree:
This is a self-balancing binary search tree in which each node contains an extra bit for denoting the color of the node, either red or black.
It satisfies the following properties:

1. Every node is either red or black.
2. The root is black
3. Every leaf (NIL) is black
4. If a red node has children, then the children are always black
5. For each node, any simple path to any of its descendant leaf has the same black-depth

## How the red-black tree is self-balancing:
The limitations put on the node colours ensure that any simple path from the root to a leaf is not more than twice as long as any other such path. 

## Operations performed in a red-black tree:
We can do a `left rotation`, `right rotation`, `Left right rotate` and `left right rotate`.

### Inserting an element on to a red-black tree:
While inserting a new node, the new node is always inserted as a red node. After which, if the tree is violating the properties of the red-black tree then, we do the following operations:
1. Recolor
2. Rotation

## Algorithm to insert a node:
1. Let `y` be the leaf(`NIL`) and `x` be the root of the tree. 
2. Check if the tree is empty...ie whether `x` is `NIL`. If yes, insert a new node as a root node and color it black.
3. Else, repeat the steps until leaf, `NIL` is reached. 
    - Compare `newKey` with the `root key`.
    - If the `newKey` is greater than `root key` then traverse through the right subtree.
    - Else travers through the left subtree
4. Assign a parent of the leaf as a parent of the `new node`.
5. If `leaf key` is greater than `new key`, then make it a `right child`
6. Else make it a `left node`. 
7. Assign `NULL` to the left and right child of the `new node`.
8. Assign the color `RED` to the `new node`.
9. Call InsertFix algorithm to maintain the property of the property of red-black tree if violated.

## Why the inserted node is always RED:
This is because inserting a red node does not violate the depth property of a red-black tree. 
If one attaches a red node to a red node, then the rule is violated but it is easier to correct this than depth problem.

## Algorithm to maintain red-black property after insertion:
1. Do the following if the parent of the new node `p` is RED.
2. If `p` is the left child of `grandParent gP` of `z`, do the following:
    - case I:
        - If the colour of the right child of gP of z is red, set the color of both chidren of gP to black and the colour of gP to red
        Assign gP to `newNode`
    - Case II:
        - Else if the new node is the right child of P, then assign p to `newNode`.
        - left-rotate `newNode`
    - Case III: 
        - set the colour of P as black and gP as red
        - right-rotate gP
3. Else do the following:
    - If the colour of the left child of gP of z is red, set the colour of both children of gP as black and the colour of gP as red
    - Assign gP to new node
    - Else if new node is the left child of p, then, assign p to new node and right-rotate new node.
    - Set the colour of p as black and colour of gP as red.
    - Left rotate gP
4. Set the root of the tree as black.

## Deleting a node:
1. Save the colour of `nodeToBeDeleted` in `originalColour`
2. If the left child of `nodeToBeDeleted` is NULL:
    - Assign the right child of `nodeToBeDeleted` to `x`
    - Transplant `nodeToBeDeleted` with `x`
3. Else if the right child of `nodeToBeDeleted` is NULL:
    - Assign the left child of `nodeToBeDeleted` to `x`
    - Transplant `nodeToBeDeleted` with `x`
4. Else:
    - Assign the minimum of right sub-tree of `nodeToBeDeleted` into `y`
    - Save the colour of `y` into `originalcolour`
    - Assign the right child of `y` into `x`
    - If y is a child of `nodeToBeDeleted`, then set the parent of `x` as `y`
    - Else transplant `y` with rightchild of `y`
    - Transplant `nodeToBeDeleted` with `y`
    - Set the colour of `y` to `originalcolour`
5. If `originalcolour` is black, then call DeleteFix(x)

## Algorithm to maintain red-black property after deletion:

This algorithm is implemented  when a black node is deleted because it violates the black depth property
This violation is corrected by assuming that node `x` (which is occupying `y`'s original position) has an eSxtra black. This makes `x` neither red nor black. It is either doubly black or black-and-red.

However, the colour attibute of `x` is not changed rather the extra black is represented in `x` 's pointing to the node.

The extra black can be removed if:
1. It reaches the root node
2. If `x` points to a red-black node. In this case, `x` is coloured black.
3. Suitable rotations and recolourings are performed.

To retain the properties of a red-black tree:
1. Do the following until `x` is not the root of the  and the colour of `x` is black.
2. If `x` is the left child of its parent:
     - Assign `w` to the sibling of `x`
     - If the right chilf of the parent of `x` is red:
    - Case I:
        - Set the colour of the right child of the parent of `x`as black
        - Set the colour of the parent of `x` as red
        - left-rotate the parent of `x`
        - Assign the right child of the parent of `x` to `w`
    - If the colour of both the left and right child of `w` is black:
    - Case II:
        - Set the colour of `w` as red
        - Assign the parent of `x` to `x`
    - Else if the colour of the rightchild of `w` is black:
    - Case III:
        - Set the colour of the left child of `w` as black
        - set the colour of `w` as red
        - right-rotate `w`
        - assign the right child of the parent of `x` to `w`
    - If any of the above cases do not occur:
    - Case IV:
        - Set the colour of `w` as the colour of the parent of `x`
        - Set the colour of the parent of `x` as black
        - Set the colour of the right child of `w` as black
        - left-rotate the parent of `x`
        - Set `x` as the root of the tree
3. Else the same as above with right changed with left and vice-versa.
4. Set the colour of `x` as black.