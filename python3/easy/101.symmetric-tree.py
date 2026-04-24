# LeetCode Solution
# Problem: 101. Symmetric Tree
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/symmetric-tree/
# Submitted: 2026-04-19 00:38:56 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(a, b):

            if not a and not b:
                return True

            if not a or not b:
                if not a and b:
                    return False
            
                if a and not b:
                    return False

            if a.val != b.val:
                return False
            
            if a.val == b.val:
                return dfs(a.left, b.right) and dfs(a.right, b.left)

        return dfs(root.left, root.right)
