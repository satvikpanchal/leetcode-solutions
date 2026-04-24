# LeetCode Solution
# Problem: 695. Max Area of Island
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/max-area-of-island/
# Submitted: 2026-04-24 04:39:06 UTC
# Status: Accepted

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):

            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in seen or grid[r][c] == 0:
                return 0

            seen.add((r, c))
            
            return (1 +
            dfs(r + 1, c) + 
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))

        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = dfs(r, c)
                    res = max(res, area)

        return res