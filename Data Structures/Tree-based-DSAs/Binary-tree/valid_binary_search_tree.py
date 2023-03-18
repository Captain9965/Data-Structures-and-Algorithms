"""
    validate a binary search tree:
        1. duplicate values invalidate the binary tree
    

"""

"""
    space and time analysis:
        space: O(n)
        time: O(n)

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(self, root: TreeNode):
    return validate_bst(root)

def validate_bst(root : TreeNode, maximum = float('inf'), minimum = float('-inf')):
    if not root:
        return True
    if root.val <= minimum  or root.val >= maximum:
        return False
    return validate_bst(root.left, root.val, minimum) and \
        validate_bst(root.right, maximum, root.val) 

