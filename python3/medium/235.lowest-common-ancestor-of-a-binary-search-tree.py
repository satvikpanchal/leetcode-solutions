# LeetCode Solution
# Problem: 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Submitted: 2025-10-04 02:19:13 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current
            
        