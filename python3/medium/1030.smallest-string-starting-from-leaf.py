# LeetCode Solution
# Problem: 1030. Smallest String Starting From Leaf
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Submitted: 2026-04-13 02:48:04 UTC
# Status: Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path, best):
            if not node:
                return best

            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                candidate = "".join(path[::-1])
                if best == "" or candidate < best:
                    best = candidate
            else:
                best = dfs(node.left, path, best)
                best = dfs(node.right, path, best)

            path.pop()
            return best

        return dfs(root, [], "")
