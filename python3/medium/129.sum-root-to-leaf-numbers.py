# LeetCode Solution
# Problem: 129. Sum Root to Leaf Numbers
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Submitted: 2026-04-13 00:36:59 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS problem recursion
        # list of numbers (numbers from root to the leaf node of the tree)
        # add up all the answers
        res = []

        def dfs(root, cur):
            # 1
            if not root:
                return
            
            if not root.left and not root.right:
                # print(root.val)
                # print(cur)
                cur.append(str(root.val))
                res.append(int("".join(cur[:])))
                cur.pop()
                return

            cur.append(str(root.val))
            dfs(root.left, cur)
            dfs(root.right, cur)
            cur.pop()

        dfs(root, [])   

        return sum(res)



            

