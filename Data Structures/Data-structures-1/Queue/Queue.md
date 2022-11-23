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

##  Limitations of the queue:
After the rear reaching the last element, we can only add a elements to the lower indices only after the queue has been reset. This is overcome by a special type of queue called a **circular queue**.

## Time-space analysis:

When implemented using arrays, the enqueue and dequeue operations occur in 0(1) time. When implemented using python lists, the pop() operation may take 0(n) time depending on the position of item to be popped.

## Queue applications:

1. Disk scheduling, cpu scheduling operations
2. Used for synchronization when data is sent between 2 processes asynchronously.
3. Handling of interrrupts in real-time systems
4. Call centre phone systems.

## Types of queues:

>1. Simple queues - As above.
>2. Circular queues - The last element points to the first element and therefore, one can insert an element in the first position when the last position is occupied. Has the benefit of better memory utilization.
>3. Priority queue- Each element is associated with a priority and are served accordingly. If elements with the same priority occur, they are served according to the order they occur in the queue.
>4. Dequeue - This is a double-ended queue where insertion and deletion can occur from either end of the queue. It does not follow the FIFO rule.


