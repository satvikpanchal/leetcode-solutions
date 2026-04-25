# LeetCode Solution
# Problem: 1073. Number of Enclaves
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-enclaves/
# Submitted: 2026-04-25 21:02:26 UTC
# Status: Accepted

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # seen = set()
        res = 0
        row = len(grid)
        col = len(grid[0])
        is_boundary = False

        def dfs(r, c):
            nonlocal is_boundary

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return 0

            if r == 0 or r == row - 1 or c == 0 or c == col - 1:
                is_boundary = True
            
            grid[r][c] = 0

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:
                    ans = dfs(i, j)
                    grid[i][j] = 0

                    if is_boundary == True:
                        ans = 0
                        is_boundary = False

                    res += ans

        return res
