# Circular Queue:

In this data structure, the first element is connected to the last element. It solves the major problem of the simple queue which is poor space utilization.

## How it works:

Works on the principle of circular increment. When one tries to increment the pointer and we are at the end of the queue, we start from the beginning of the queue. 

## Circular queue operations:

The front and rear values are initially set to -1

### Enqueue:
- check if the queue is full
- circularly increase the rear index by 1, and if it reaches the end, next it would be at the start of the queue.
- add the new element in the rear position.

### dequeue:
- check if it is empty.
- circularly increase the front index by 1 
- for the last element, reset the values of front and rear to -1.
- Check for the full queue has 1 additional case: when  `front = rear + 1` apart from the expected: `front == 0 && rear = size -1`

## Applications of circular queue:
>- Cpu scheduling
>- Memory management
>- Traffic management
