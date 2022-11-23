# Double ended queue implementation in python:
# to be improved...by adding fixed size and proper rear and front tracking

class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)
        pass

    def addFront(self, item):
        self.items.insert(0, item)
        pass

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
if __name__ == "__main__":
    dq = Dequeue()
    for i in range(0, 5):
        dq.addFront(i)
    print(dq.items)

    for i in range(0, 5):
        dq.addRear(i * 4)
    print(dq.items)