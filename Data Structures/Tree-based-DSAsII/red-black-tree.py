""" Red black tree in python: """

import sys
import enum

class color(enum.Enum):
    RED = 1
    BLACK = 0


#Node creation:
class Node:
    def __init__(self, item):
        self.color = color.RED.value
        self.item = item
        self.parent = None
        self.left = None
        self.right = None

#Red black tree:
class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = color.BLACK.value
        self.TNULL.left = None
        self.TNULL.right = None 
        self.root = self.TNULL

    def pre_order_helper(self, node):
        

if __name__ == "__main__":
    newNode = Node(20)