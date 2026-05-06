# LeetCode Solution
# Problem: 513. Find Bottom Left Tree Value
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-bottom-left-tree-value/
# Submitted: 2026-04-27 19:39:11 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        res = 0

        while q:
            node = q.popleft()

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return node.val
                