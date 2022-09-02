#circular queue implementation in python:

class CircularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.queueReset()

    def isFull(self):
        return ((self.rear + 1) % self.size == self.front)
    def isEmpty(self):
        return(self.front == -1) 
    def justEmpty(self):
        return(self.rear == self.front)
    def queueReset(self):
        self.front = self.rear = -1
    def enqueue(self, data):
        if(self.isFull()):
            print("The queue is already full!")
        elif(self.isEmpty()):
            print("The queue is empty")
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if(self.isEmpty()):
            print("The queue is already empty")
        if(self.justEmpty()):
            dequeued_value = self.queue[self.front]
            self.queueReset()
            return dequeued_value
        else:
            dequeued_value = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return dequeued_value
    def printCircularQueue(self):
        if (self.isEmpty()):
            print("The queue is empty!")
        elif(self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

if __name__ == "__main__":
    cQueue = CircularQueue(5)
    for i in range(10):
        cQueue.enqueue(i)
    cQueue.printCircularQueue()
    for i in range(2):
        cQueue.dequeue()
    cQueue.printCircularQueue()
