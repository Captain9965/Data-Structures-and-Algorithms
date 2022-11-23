class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        if(self.isfull()):
            print("The queue is full")
            return
        self.queue.append(item)
        print("Appended item is " + str(item))
        return str(item)
    def isfull(self):
        return len(self.queue) > 4 #Note that here max_length is 5
    def isEmpty(self):
        return len(self.queue) < 1
    def dequeue(self):
        if (self.isEmpty()):
            print("Queue is already empty")
            return None
        self.queue.pop(0)
    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    q = queue()
    q.enqueue(34)
    q.enqueue(67)
    q.enqueue(90)
    q.enqueue(900)
    q.enqueue(78)
    q.enqueue(67)

    q.printQueue()

    for i in range(10):
        q.dequeue()
    
