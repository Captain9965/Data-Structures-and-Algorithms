""" 
    count the number of nodes present in a full and complete binary tree in O(log n ) time complexity:
"""
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 
    space and time complexity is:
        space: O(1)
        time: O(log ^ 2 n)
"""
def count_nodes(root: TreeNode):
        if not root:
            return 0
        
        height = 0

        currentNode = root

        """ find height of tree: """
        while (currentNode.left):
            height += 1
            currentNode = currentNode.left

        if height == 0:
            return 1
        
        total_nodes = pow(2, height) - 1

        left = 0
        right = total_nodes
        idx = 0
        
        while left < right:
            currentNode = root
            l = 0
            r = total_nodes 
            idx = math.ceil((left + right)/ 2)
        
            for _ in range(height):
                mid = math.ceil((l + r)/ 2)

                if idx >= mid:
                    currentNode = currentNode.right
                    l = mid
                else:
                    currentNode = currentNode.left
                    r = mid - 1 
            if currentNode:
                left = idx
            else:
                right = idx - 1
        
        return total_nodes + left + 1