"""
    Imagine you are standing on the right of a binary tree, 
    return the nodes you can see from top to bottom in an array


"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def right_side_view(root):
    result = []
    fill_right_side_view(root, result)
    return result

def fill_right_side_view(root: Node, result, level = 0):
    if root is None:
        return
    level += 1
    if len(result) < level:
        result.append(root.val)
    else:
        result[level - 1] = root.val
    fill_right_side_view(root.left, result, level)
    fill_right_side_view(root.right, result, level)

""" 
    space and time analysis ->
        time is O(n)
        space complexity is O(n)


"""

def fill_right_side_view_prioritize_right(root: Node, result, level = 0):
    if root is None:
        return
    level += 1
    if len(result) < level:
        result.append(root.val)
    if root.right:
        fill_right_side_view(root.right, result, level)
    if root.left:
        fill_right_side_view(root.left, result, level)