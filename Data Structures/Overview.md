# Overview of data structures:
A data structure refers to a way of organizing data in a computer so that it can be used effectively. <br>
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
- Register stack - this is a memory element present in the memory unit and it is very small in size.
- Can handle a very large amount of data and is flexible in size.






