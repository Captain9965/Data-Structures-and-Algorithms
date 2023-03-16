""" 
    Write an algorithm that returns the maximum depth of a binary tree



"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


"""
    Time complexity is O(n) worst case if unbalanced
    space complexity is O(n) worst case if unbalanced

"""

def max_depth(node : Node, count):
    if not node:
        return count
    count += 1
    return max(max_depth(node.right), max_depth(node.left))
