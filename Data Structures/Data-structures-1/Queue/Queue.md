# Queue:

This is a data structure that follows the FIFO rule. Addition of items is called to enqueue while removal of items is called to dequeue.

## Basic queue operations:

1. Enqueue: adding and element to the end of the queue
2. Dequeue: add and element to the front of the queue
3. isEmpty: check if queue is empty
4. isFull: check if queue is full
5. peek: check the front value of the queue without removing it.

## Working of the queue:
1. Two pointers **front** and **rear** track the first element of the queue respectively. Both initially set to -1
2. For the enqueue operation,check whether the queue is full,  increase the front value by 1 and the rear also, for the first element and let the rear point to the added element.
3. for a dequeue operation, check whether the queue is empty, return the value pointed to by front, increase the front index by 1,for the last elemtent, reset the values of front and rear to -1.
4. 
