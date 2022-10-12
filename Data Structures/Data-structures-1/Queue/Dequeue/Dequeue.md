# Double ended queue:

Insertion or removal of elements can either occur from the front or rear.

## Types of dequeues:
1. Input restricted - input is restricted at one end but removal can occur at both ends

2. Output restricted - output is restricted at one end but insertion can occur at both ends.

## Operations of a dequeue:

In a circular implementaion, if the array is full, we start from the beginning, whereas in a linear implementation, no more elements can be inserted when full. 

> Take an array of size n
>
> set 2 pointers at the first position and set front = -1 and rear = 0
> 
> To insert at front, 
>> Check the position of front
>>
>> If front < 1, then reinitialize front = n - 1 (last index)
>> else decrease front by 1 
>>
>> Add new key into array[front]

> To insert at the rear:
>> Check if the array is full
>> 
>> If full, reinitialize rear = 0
>>
>> Else increase rear by 1
>>
>> Add new key to array[rear]

> To delete from the front:
>> check if dequeue is empty:
>>
>> ie. front = -1, then deletion cannot be performed
>>
>> If the dequeue only has 1 element ie front = rear, then set front = rear = -1
>>
>> else if front is at the end, ie front = n-1 , set front =0
>> 
>> else front = front + 1

> Deletion from the rear:

>> check if dequeue is empty, ie front = -1
>>
>> If dequeue has only one element, then set front = rear = -1
>>
>> if rear is at the front ie = 0, then set rear = n - 1
>>
>> else rear = rear - 1 

> Check empty:
>> If front = -1, then the queue is empty

> Check full:
>> If front = 0 and rear = n - 1, or if front = rear + 1    


## Space time complexity:

Is 0(1) for all operations

## Application of a dequeue:
1. Undo operations in browsers
2. Storing history in browsers
3. Implementing both stacks and queues

