# LeetCode Solution
# Problem: 515. Find Largest Value in Each Tree Row
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Submitted: 2026-04-16 04:31:07 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            curMax = float('-inf')

            for i in range(0, qLen):
                node = q.popleft()

                if node:
                    if curMax <= node.val:
                        curMax = node.val
                    q.append(node.left)
                    q.append(node.right)
                    
            res.append(curMax)

        res.pop()

        return res