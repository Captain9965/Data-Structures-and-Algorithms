from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = []
        averages = []
        queue.append(root)
        level_count = len(queue)
        process_count = 0
        sum_so_far = 0
        while queue:
            node = queue.pop(0)
            sum_so_far = sum_so_far + node.val
            process_count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if process_count == level_count:
                #calculate average and append to result list:
                avg = (sum_so_far / level_count)
                averages.append(avg)
                sum_so_far = 0
                process_count = 0
                level_count = len(queue)
            
        return averages