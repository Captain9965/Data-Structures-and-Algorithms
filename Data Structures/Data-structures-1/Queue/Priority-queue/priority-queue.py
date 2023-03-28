""" Priority queue application in python: """
""" sift down function:"""

import math
class  PriorityQueue:
    def __init__(self, isMaxHeap = True):
        self.array = []
        self.isMax_heap = isMaxHeap
    def size(self):
        return len(self.array)
    def peek(self):
        return self.array[0]
    def isEmpty(self):
        return len(self.array) == 0
    def parent(self, idx):
        return math.floor((idx - 1) / 2)
    def leftChild(self, idx):
        return (idx * 2) + 1
    def rightChild(self, idx):
        return (idx * 2) + 2
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    def compare(self, i, j):
        if self.isMax_heap:
            return self.array[i] > self.array[j]
        else:
            return self.array[i] < self.array[j]
    def push(self, value):
        self.array.append(value)
        self.siftUp()
        return self.size
    def siftUp(self):
        nodeIdx = self.size() - 1
        while(nodeIdx > 0 and self.compare(nodeIdx, self.parent(nodeIdx))):
            self.swap(nodeIdx, self.parent(nodeIdx))
            nodeIdx = self.parent(nodeIdx)
    def pop(self):
        if self.isEmpty():
            return None
        self.swap(0, self.size() - 1)
        val = self.array.pop()
        self.siftDown()
        return val
    def siftDown(self):
        nodeIdx = 0

        while ((self.leftChild(nodeIdx) < self.size()) and self.compare(self.leftChild(nodeIdx), nodeIdx) or
            (self.rightChild(nodeIdx) < self.size()) and self.compare(self.rightChild(nodeIdx), nodeIdx)):
            greaterChildIdx = self.rightChild(nodeIdx) if (self.rightChild(nodeIdx) < self.size() and self.compare(self.rightChild(nodeIdx), self.leftChild(nodeIdx))) \
                            else self.leftChild(nodeIdx)
            self.swap(greaterChildIdx, nodeIdx)
            nodeIdx = greaterChildIdx
    def printQueue(self):
        for i in range(len(self.array)):
            print(self.array[i], end= " ")
        print()

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(15)
    pq.push(12)
    pq.push(50)
    pq.push(7)
    pq.push(40)
    pq.push(22)

    while not pq.isEmpty():
        print(pq.pop())

