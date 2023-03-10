""" 

    Implement a queue with stack only standard operations with at most 2 stacks.

"""



class MyQueue:

    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        if not self.empty():
            self.stack.reverse()
            value = self.stack.pop()
            self.stack.reverse()
            return value
        else:
            return None

    def peek(self) -> int:
        if not self.empty():
            return self.stack[0]
        else:
            return None

    def empty(self) -> bool:
        return len(self.stack) < 1

class MyQueueWithStacks:
    """ Queue takes up O(n) space"""
    def __init__(self):
        self.In = []
        self.Out = []

    """ O(1) for both time and space """
    def push(self, x :int):
        self.In.append(x)

    """ Time is O(n) and space is O(1)"""
    def pop(self):
        if len(self.Out):
            return self.Out.pop()
        if len(self.In):
            while len(self.In):
                self.Out.append(self.In.pop())
            return self.Out.pop()
        else:
            return None
        
    """ Time is O(n) and space is O(1)"""
    def peek(self):
        if not self.empty():
            if len(self.Out):
                return self.Out[len(self.Out) - 1]
            if len(self.In):
                while len(self.In):
                    self.Out.append(self.In.pop())
                return self.Out[len(self.Out) - 1]
        else:
            return None
        
    """ Time is O(1)"""
    def empty(self):
        return len(self.In) < 1 and len(self.Out) < 1
            



if __name__ == "__main__":
    queue = MyQueueWithStacks()
    queue.push(2)
    queue.push(3)
