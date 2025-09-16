# LeetCode Solution
# Problem: 200. Number of Islands
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-islands/
# Submitted: 2025-09-11 01:01:07 UTC
# Status: Accepted

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()

        islands = 0

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                row0, col0 = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row0 + dr, col0 + dc

                    if (r in range(row) and
                        c in range(col) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):

                        q.append((r, c))
                        visited.add((r, c))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands
