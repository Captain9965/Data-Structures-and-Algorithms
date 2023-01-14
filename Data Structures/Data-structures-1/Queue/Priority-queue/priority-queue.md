# PRIORITY QUEUE:

In this data structure, each element is associated with a priority value. And elements are served on the basis of their piority. If elements have the same priority, they are served according to their order in the queue.

Generally, the value of the element is considered its priority. For example, the element with the highest value is considered highest priority.

## Implementation:

Can be implemented using an array, linked list, a heap data structure or a binary search tree. Of all of this, the heap data structure provides the most efficient Implementation.

## Operations of a priority queue:
### Inserting:
1. Insert the element at the end of the tree.
2. heapify the tree

### Deleting an element:
1. Select the element to be deleted.
2. Swap it with the last element.
3. Remove the last element.
4. Heapify the tree.

### peeking from the priority queue:
This is always the root node whether for min or max heap.

### Extracting the min/max value:
return the rootnode after removing the rootnode.
```
Operations	        peek	insert	    delete
Linked List	        O(1)	O(n)	    O(1)
Binary Heap	        O(1)	O(log n)	O(log n)
Binary Search Tree	O(1)	O(log n)	O(log n)
```
### Priority queue applications:
1. Dijkstra's algorithm.
2. implementing a stack.
3. load balancing and interrupt handling in operating systems.
4. data compression in Huffman code.