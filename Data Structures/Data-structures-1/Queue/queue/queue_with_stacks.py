""" 

    Implement a queue with stack only standard operations with at most 2 stacks.

"""

class MyQueue:

    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stack = self.stack.reverse()

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
        else:
            return -1

    def peek(self) -> int:
        if not self.empty():
            return self.stack[len(self.stack) - 1]
        else:
            return -1

    def empty(self) -> bool:
        return len(self.stack) < 1

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(2)
    queue.push(3)
