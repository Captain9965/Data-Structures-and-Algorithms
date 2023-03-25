
""" My priority queue for O(log n ) insertion and popping 
    Note that we have in this implemantation, we allow duplicate values..
"""

import math
class  PriorityQueue:
    def __init__(self, comparator):
        self.array = []
        self.comparator = comparator
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
        self.comparator(self.array[i], self.array[j])
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

def build_adj_list(times: list, adjList: list):
    for travel_time in times:
        adjList[travel_time[0] - 1].append([travel_time[1] - 1, travel_time[2]])


"""space and time complexity: 
    Space is O(E + N)
    time is O(N + E log E)

    Note that Djikstra's does not work with negative weights...and negative cycles
    since values could perpetually update.
"""


def networkTimeDelay(times: list,n , k):
    adjList = [[] for i in range(n)]
    distances = [float('inf') for i in range(n)]
    distances[k - 1] = 0
    queue = PriorityQueue(lambda a, b: distances[a] < distances[b])
    build_adj_list(times, adjList)
    queue.push(k - 1)
    print(distances)

    while(not queue.isEmpty()):
        currentNode = queue.pop()
        neighbours = adjList[currentNode]
        for neighbour in neighbours:
            neighbouring_node = neighbour[0]
            weight = neighbour[1]
            if distances[currentNode] + weight < distances[neighbouring_node]:
                distances[neighbouring_node] = distances[currentNode] + weight
                queue.push(neighbouring_node) 
                

    ret = max(distances)
    if ret == float('inf'):
        return -1
    return ret


""" with Bellman Ford algorithm: 

    only drawback of is that it is susceptible to negative cycles...but if
    we have one more loop -> n we can detect if we have any updates to detect this...

    space complexity is O(N)
    time complexity is O(EN)

"""

def networkTimeDelayBellmanFord(times: list, n, k):
    distances = [float('inf') for i in range(n)]
    distances[k - 1] = 0

    for i in range(n - 1):
        updated = False
        for edge in times:
            if distances[edge[0] - 1] + edge[2] < distances[edge[1] - 1]:
                distances[edge[1] - 1] = distances[edge[0] - 1] + edge[2]
                updated = True
        if not updated:
            break
 
    ret = max(distances)
    if ret == float("inf"):
        return -1
    return ret

    
if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    print(networkTimeDelayBellmanFord(times, 4, 2))