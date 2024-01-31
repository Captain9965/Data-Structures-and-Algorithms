"""
    find the kth smallest element within a binary tree...Leetcode question:

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result_list = []
        number_tracker = [0]
        dfs(root, result_list, k, number_tracker)
        return result_list[0]

def dfs(root, result_list, k, n):
    if root.left:
        dfs(root.left, result_list, k, n)
    if root:
        n[0] += 1
        print(root.val, n)
        if n[0] == k:
            result_list.append(root.val)
            return 
    if root.right:
        dfs(root.right, result_list, k, n)