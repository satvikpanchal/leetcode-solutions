# LeetCode Solution
# Problem: 695. Max Area of Island
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/max-area-of-island/
# Submitted: 2026-04-24 04:49:42 UTC
# Status: Accepted

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            return (1 +
            dfs(r + 1, c) + 
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))

        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)

        return res