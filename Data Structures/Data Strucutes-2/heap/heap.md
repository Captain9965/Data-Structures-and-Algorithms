# Heap Data structure:
This is a complete binary tree which satisfies the heap property where any given node is:

1. always greater than its child node(s) and the key of the root node is the largest among other nodes. This is called the **max heap property**.
2. Always smaller than its child noe(s) and the key of the root node is the smallest among all other nodes.This property is called the **min heap property**.

## Heap Operations
### Heapify:
This is the process of creating a heap data structure from a binary tree. It is used to create a min-heap or a max-heap. Procedure:
1. Create a complet binary tree from an array 
2. Start from the first index of the non-leaf node whose index is given by `n/2 - 1`.
3. Set the current element `i` as the largest.
4. The index of the left child is given by `2i + 1` and the index of the right child is given by `2i + 2`. If the `left child` is greater than the `current element`, set the `leftchildindex` as the largest. If the `right child` is greater than the element in `largest`, set the `rightchildindex`as `largest`
5. Swap the `largest` with the `currentElement`.
6. Repeat 2-6 until the sub-trees are also heapified.

For min-heap, both the `leftchild` and the `rightchild` must be larger than the parent for all the nodes.

### Inserting elements into a heap:
Algorithm:

```
If there is no node, 
  create a newNode.
else (a node is already present)
  insert the newNode at the end (last node from left to right.)
  
heapify the array
```

1. Insert the new element at the end of the tree
2. Heapify the tree.
3. For min-heap, the algorithm is modified such that parent node is always smaller than new node.

### Delete element from Heap:
Algorithm:
```
If nodeToBeDeleted is the leafNode
  remove the node
Else swap nodeToBeDeleted with the lastLeafNode
  remove noteToBeDeleted
   
heapify the array
```
1. Select the element to be deleted.
2. Swap it with the last element.
3. Remove the last element.
4. Heapify the tree.

For min-heap, the algorithm is modified such that the `childnodes` are always greater than the `current node`.

### Peek(Find(min/max)):
 Returns the maximum element from a max-heap or the minimum element from a min-heap.
 This is always the root node for both cases.

 ### Extract-Max/Min:
Extract-Max returns the max value node after removing it from a Max heap while Extract-Min returs the mim value node after removing it from a Min heap.

### Applications of Heap Data structure:
1. Implementing priority queues
2. Dijkstra's algorithm.
3. Heap sort.