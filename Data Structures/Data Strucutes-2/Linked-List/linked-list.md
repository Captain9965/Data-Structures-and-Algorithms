# Linked List:
This is a linear data structures that includes a series of interconnected nodes where each node stores data and the address of the next node. 

The first node is called HEAD and the last one is identified since its next is pointing to NULL. 

linked lists could be of many types like `singly linked lists`, `doubly linked list`, and `circular linked list`

## Representation of a linked list (singly linked list):

Constructing a linked list:
>1. Initialize the nodes after declaring a node as a struct of data item and a next node reference
>2. Allocate memory for all the nodes
>3. Assign data values
>4. Connect nodes

The true power of a linked list is the fact that one can break the chain and rejoin it as required. for example, when adding nodes in between. Just update the next pointer of the preceding node and set the next pointer of the node to be added to be the one the preceding node pointed to. 


## Space Time complexity:

1. Search is 0(n) 
2. Insertion and deletion is 0(1)


Space complexity is 0(n)

## Linked list applications:
1. Dynamic memory allocation
2. Implemented in stack and queue
3. Undo functionality if softwares
4. Hashtables and graphs

## Linked list operations:

There are various operations like **sorting, inserting, deleting, search and traversal**

### 1. Traversal:

We display the contents of a temp node until it becomses NULL, then we break out of the loop.

### 2. Inserting elements at the beginning:
1. Create the new node and allocate memory accordingly
2. Store data in the new node
3. Change the next of the new node to point to the current head.
4. Change the head to point to the newly created node.

### 3. Inserting at the end:
1. Allocate memory to the new node and store data.
2. Traverse to the last node.
3. Change the next of the last node to the new node.

### 4. Inserting at the middle:

1. Allocate memory to the new node and store data
2. Traverse to the node just before the required position of the new node.
3. Change the next pointers to include the new nodes in between.

### 5. Deleting from a linked list:

1. Deleting from the beginning:

Point HEAD to the second node.

2. Deleting from the end:

Traverse to the second last element then change its next pointer to NULL.

3. Deleting from the middle:

Traverse to the element before the element to be deleted.
Update the next pointers to exclude the node from the chain

### 6. Searching for an element in a linked list:

1. Make head as the current node.
2. Loop until the current node is NULL.
3. In each iteration, check whether the key of the node is equal to item. If they are a match, return true, otherwise false. 

### 7. Sorting elements in a linked list:

A simple sorting algorithm, called Bubble Sort can be used to sort the elements in ascending order:
 1. Make head as the current node and create another node INDEX for later use.
 2. if HEAD is NULL return.
 3. Else run a loop until the last node.
 4. In each iteration, do steps 5 and 6:
 5. Store the next node of current in INDEX. 
 6. Check whether the data of the current node is greater than that of index. If greater, swap current and index

 ## Types of linked lists:

 ### Singly linked list:
 Each node has data and a pointer to the next node.

 ### Doubly linked list:
 In this, we add a pointer to the previous node, therefore meaning that we can go in either direction, forwards or backwards

 ### Circularly linked list:
 The last element is linked to the first element. This forms a circular loop. 
 It can either be singly linked or doubly linked.

 For singly linked lists, the next pointer of the last node points to the first node. For doubly linked list, the previous pointer of the first element points to the last element as well.
 
  


