# LeetCode Solution
# Problem: unknown. Validate Binary Search Tree
# Difficulty: Unknown
# Language: Python3
# URL: https://leetcode.com/problems/validate-binary-search-tree/
# Submitted: 2026-05-01 01:47:21 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, low, high):
            if not root:
                return True
            
            if root.val <= low or root.val >= high:
                return False

            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

        return dfs(root, float("-inf"), float("inf"))