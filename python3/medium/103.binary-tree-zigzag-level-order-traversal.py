# LeetCode Solution
# Problem: 103. Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Submitted: 2026-04-15 05:18:13 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)
        flag = False
        
        while q:
            qLen = len(q)
            level = []

            for i in range(0, qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                if flag == False:
                    res.append(level)
                    flag = True
                elif flag == True:
                    res.append(level[::-1])
                    flag = False

        return res