# LeetCode Solution
# Problem: 637. Average of Levels in Binary Tree
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Submitted: 2026-05-05 23:32:50 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()
        q.append(root)
        res = []
        elements = 0
        level_total = 0

        while q:
            qLen = len(q)

            for i in range(0, qLen):
                node = q.popleft()

                if node:
                    elements += 1
                    level_total += node.val
                
                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
            
            if elements:
                res.append(level_total/elements)
                elements = 0
                level_total = 0
        
        return res