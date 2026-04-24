# LeetCode Solution
# Problem: 1254. Deepest Leaves Sum
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/deepest-leaves-sum/
# Submitted: 2026-04-15 05:18:07 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        res = 0

        while q:
            qLen = len(q)
            res = 0

            for i in range(0, qLen):
                node = q.popleft()

                if node:
                    res += node.val

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        return res
