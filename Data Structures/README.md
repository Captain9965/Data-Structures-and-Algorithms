# Overview of data structures:
A data structure refers to a way of organizing data in a computer so that it can be used effectively. <br>
There are 2 types of data structures. Linear and non-linear
## Non-linear
- Tree
- Graph

## Linear Data Structures:
They consist of: 

- Arrays
- Linked Lists
- Stack
- Queues

### 1. Array:
This is a data structure used to store homogenous elements in contiguous locations.

> Lets say the size of an array is n:
>
>- Accessing time is 0(1) since the the elements are stored in contiguous memory locations
>
>- 0(n) for sequential search and 0(log n) for binary search if array is sorted.
>- 0(n) for insertion time especially when inserting at the beginning since all elements have to be shifted 
>- 0(n) for deletion of elements when elements have to be shifted.

### 2. Linked List:
A linked list is a data structure where each element is a node containing data and a reference to the next node in the form of pointers. Can grow and decrease as required 

#### Types of linked lists:
>1. Singly linked list:<br>
In this one, every node stores a reference to the next node and the last node has the reference as NULL
>2. Doubly linked list:
In this one, every node has, in addition to a reference to the next element, a reference to the previous element.the upside is that we can traverse in both directions and we don't have to have access to the previous node for reference.
>3. Circular linked list:
In this one, there is no end element NULL, used to implement circulat queues. Could be circular singly or doubly linked.
>> For the circular doubly linked list,<br>
>>- The access time is 0(n)
>>- Seach time is 0(n)
>>- Insertion time 0(1) if we are at the insertion position
>>- Element deletion time of 0(1) if we know the previous node to the node to be deleted

The main advantage of a linked list is that it is space efficient and the main drawback is that randomn access is not allowed.

###  3. Stack:
This is a LIFO data structure which is an abstract data type which serves as a collection of elements, with 2 principal operations..push, which adds an element to the top of the stack and pop which removes the last element that was added. Both are performed at the same end of the stack and can be an array or a linked list.

Time analysis:
>- Insertion and deletion: 0(1)
>- Access time 0(n) worst case scenario

Used for maintaining function calls, check for balanced parenthesis, and the undo operation in editors. Also used in the back operation in browsers.
#### Primary stack operations:
>1. void push(int data)
>2. int pop()
#### Auxiliary stack operations:
>1. top()- will return the element at the top of the stack without removing it.
>2. int size()- will return the number of elements in the stack.
>3. int isEmpty()- returns whether the stack is empty or not.
>4. int isFull()- returns whether the stack is full or not
#### Types of stacks:
- Register stack - this is a memory element present in the memory unit and it is very small in size. Can handle only a small amount of data and is limited in size
- Memory stack - Can handle a large amount of memory data and its height is flexible

### 4. Queue:

An abstract datatype that serves as a collection of elements with 2 principal operations, enqueue which is the process of adding elements to the collection from the rear side and dequeue which is the process of removing the first element that was added. 

Time space analysis:
>- insertion and deletion: 0(1)
>- Access time: 0(n) worst case

Applications of the queue:
- Cpu scheduling 
- disk scheduling
- asynchronous data transfer in pipes, and IO bufferes, file buffers
#### Basic queue operations:
>- void enqueue(int data)
>- int dequeue()

#### Auxiliary operations:
>- int front() - returns the element at the front end without removing it
>- int rear() - returns the element at the rear without removing it
>- int isEmpty() - is the queue empty or not?
>- int size() - total number of elements contained 

#### queue types:
>1. Simple - 
>2. Circular queue - The last element is connected to the last element
>3. priority queue - returns a queue with increasing order of values.
>4. dequeue - Elements can be added /removed from either end.

## Binary tree, Binary search tree, binary heap and Hash

### Binary Tree:
This is a hierarchial data structure. This is a tree data structure where each node has at most 2 children, the left and the right child, and is implemented using links

#### Representation:

A tree is represented by a pointer to the topmost node in the tree. If the tree is empty, then the root is NULL. A node contains:

1. Data
2. Pointer to left child
3. Pointer to right child

A binary tree can be traversed in 2 ways:

1. Depth first traversal: Inorder(left root right), preorder(root left right), postorder(left right root)
2. Breadth first traversal: level order traversal


binary tree properties:

1. The max number of nodes at level '1' = 2^1
2. max number of nodes = 2^h-1 -1 where h is the height of a tree which is the maximum number of edges on a path from root to leaf.
3. Minimum possible height is ceil(log2(n+1)) -1
4. Number of leaf nodes is always one more than nodes with 2 children.
5. Time complexity of tree traversal is 0(n)

Applications of binary tree:

1. Data compression algorithms (Huffman coding trees)
2. Searching for maximum or minimum in a priority queue in 0(logn) time complexity.
3. Expression trees in compilers

IN general, one could use binary trees for anything that is heirachial in nature like directories in a file, js DOM consideres the HTML page as a tree with nesting of tags as parent-child relations.





### Binary search tree:

This is a tree whose main function is to search for a specific element. This is a binary tree with the following additional properties:

1. The left sub-tree of a node contains only nodes with keys less than the node's key
2. While the right side contains only nodes with keys greater than the node's key. 
3. The left and the right subtree must also be a binary search tree. 

Time complexities:

>1. Search: 0 (h)
>2. Insertion: 0 (h)
>3. Deletion: 0 (h)
>4. Extra space: 0(n) for pointers.

If a BST is height balanced, then the h = 0 (log n)
Access search is quicker than linked lists but slower than arrays.
Insertion/deletion is quicker than arrays but slower than linked lists.

Usage:

1. Where data is constantly entering and leaving and also needs to be printed in sorted order for example in E-commerce websites 

### Binary heap:

This is a BT with the following properties:

1. Its a complete tree (all levels are completely filled except possibly the last level and the last level has all keys as left as possible)
2. It is either a min-heap or max-heap. For min-heap, the key at the root is the minimum among all keys present in the binary heap. The same must be recursively true for all nodes in the BT. 

Time complexities:

>1. get min in min heap: 0(1)
>2. extract min in min heap: 0(log n)
>3. decrease key in min heap: 0(log n)
>4. insertion: 0(log n)
>5. delete: 0(log n)

Used in implementing efficient priority queues which in turn are used for scheduling processes in operating systems. Also used in Dijkstra's and Prim's graph algorithms.

It cannot be used for searching a particular element

### Hashing:

This is a popular technique for sorting and retrieving data as fast as possible. 

why?

In BSTs, searching, inserting, and deleting takes 0 (log n) time compexity. In hashing, all the above operations can occur in 0(1) time. The worst case for hashing is 0(n) but on average, it is 0(1)

**Hash function**:

A function that is used to transform a given key into a specific slot index. If every key is mapped into a unique slot index, then that is a perfect hash function.

Properties of a good hash function:

1. Efficiently computable
2. Should uniformly distribute the keys (each table position equally likely for each key)
3. Should minimizw collisions
4. Should have a high load factor(The number of items in the table diveded by the size of the table.)

**Hash table** - This is an array of pointers to records corresponding to given value.

**Collision handling** - This is the possibility that two keys result in the same value. A collision occurs where a newly inserted key maps to an  already occupied slot in the hash table. This can be addressed by chaining and open addressing. 

Time space analysis:
>1. space: 0(n)
>2. search, insertion, deletion: 0(1), worst case: 0(n)

This may make Hashing appear far much better than BSTs. However, in hashing, elements are unordered and may be complex to implement hash tabels since generating hash functions can be difficult. In BSTs we can also easily find floor and ceil values. 

## Graphs, Trie, Segment tree and Suffix tree:
### Graph:
A graph is a data structure with the following 2 components:
1. A finite set of vertices called nodes.
2. A finite set of ordered pairs of the form (u, v) is called an edge. Edges may contain weight, value or cost.

Classifications:
1. Direction: undirected graphs where all the edges are bi-directional while in the case of directed graphs, all edges are uni-directional.
2. Weight: A weighted graph is that which a weight is associated with the edges, unlike an unweighted one. Graphs can be represented in the form of an adjacency matrix, or an adjacency list. 

The most common use of a graph is finding the shortest path in any network like routes in maps or friend suggestions based on intermediate suggestions.

### Trie:

These are efficient data structures used to search works in dictionaries. Search complexity is linear in terms of word or key length. If the keys are stored in a BST, A well balanced BST will need time proportional to M * log N where M is the maximum string length and N is the number of keys in the tree. Using the trie, we can search the trie in 0(M) time, hence much faster than BST. Hashing also provides 0(n) search time but the advantage with the trie is that there are no collisions so the worst case time complexity is 0(n). The only downside is that they require a lot of space. They are also called radix trees or prefix trees. 

Time space time complexity:
>1. Insert time: 0(M) where M is the length of the string.
>2. Search time 0(M)
>3. Space: 0(M * Alphabet size * N) where N is the number of keys in trie, and alphabet size is 26 considering only upper case latin characters.
>4. Deletion time 0(M)

Most common use of tries is dictionary searching, due to prefix search capability and implementing approximate matching algorithms used in spell checking as well as searching phones in a contact list or phone directory. 

### Segment trees:
Usually implemented when there are a lot of queries on a set of values. These queries involve min, max, updating etc. Segment trees are implemented using arrays. 

Time space analysis:
>1.Construction: 0(n)
>2. Query: 0 (Log n)
>3. Update: 0(Log n)
>4. Space: 0(n)

Application: 

Used in finding the maximum, minimum or sum of a rang of numbers.


### Suffix tree:

Used to search for a pattern in a text. The idea is to pre-process the text so that the search occurs in time linear in terms of pattern length. Pattern searching algorithms like Z, KMP take time proportional to pattern text length, which is much shorter than text length. It may not, however be the best idea for text that changes frequently like a text editor. A suffix tree is a compressed trie of all suffixes, and so to build a suffix trie from a text:

1. Generate all suffixes of the given text.
2. consider all suffixes as individual words and build a compressed trie.

Usage:

>1. Finding all occurrences of a pattern in a string.
>2. Finding the longest repeated sub-string if the text doesn't change that often. 




