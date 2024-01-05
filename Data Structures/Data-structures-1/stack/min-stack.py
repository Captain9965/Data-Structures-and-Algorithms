


""" Question:
    The MinStack is a data structure that allows for efficient retrieval of the minimum value in a stack at any given moment.
    Take note that all operations are to occur in O(1) time..
"""
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1] 
    def getMin(self) -> int:
            return self.minStack[-1]
    def printMinStack(self):
        print("Min Stack ---> ", end= " ")
        print(self.minStack)

        print("Stack --> ", end=" ")
        print(self.stack)
        
    
if __name__ == "__main__":
    instance = Solution()
    instance.push(-1)
    instance.push(5)
    instance.push(-3)
    instance.push(6)
    instance.printMinStack()
    instance.pop()
    instance.printMinStack()
