# LeetCode Solution
# Problem: 404. Sum of Left Leaves
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/sum-of-left-leaves/
# Submitted: 2026-04-16 04:21:37 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            
            if not node: 
                return 
            
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res

        

        # q = collections.deque()
        # q.append(root)
        # arr = []
        # res = 0

        # while q:
        #     qLen = len(q)
        #     level = []

        #     for i in range(0, qLen):
        #         node = q.popleft()

        #         if node.left and not node.left.left and not node.left.right:
        #             level.append(node.left.val)
                
        #         if node.left:
        #             q.append(node.left)
                
        #         if node.right:
        #             q.append(node.right)

        #     if level:
        #         arr.append(level)
        #         res += sum(level)

        # return res