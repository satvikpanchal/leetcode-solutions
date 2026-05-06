# LeetCode Solution
# Problem: 2035. Count Sub Islands
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/count-sub-islands/
# Submitted: 2026-05-06 00:13:23 UTC
# Status: Accepted

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])

        seen1 = set()
        seen2 = set()

        def dfs1(r, c):
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                (r, c) in seen1 or
                grid1[r][c] == 0
            ):
                return

            seen1.add((r, c))

            dfs1(r + 1, c)
            dfs1(r - 1, c)
            dfs1(r, c + 1)
            dfs1(r, c - 1)

        def dfs2(r, c):
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                (r, c) in seen2 or
                grid2[r][c] == 0
            ):
                return True

            seen2.add((r, c))

            valid = (r, c) in seen1

            down = dfs2(r + 1, c)
            up = dfs2(r - 1, c)
            right = dfs2(r, c + 1)
            left = dfs2(r, c - 1)

            return valid and down and up and right and left

        for i in range(row):
            for j in range(col):
                if grid1[i][j] == 1 and (i, j) not in seen1:
                    dfs1(i, j)

        res = 0

        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and (i, j) not in seen2:
                    if dfs2(i, j):
                        res += 1

        return res