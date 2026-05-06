# LeetCode Solution
# Problem: 1507. Check if There is a Valid Path in a Grid
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
# Submitted: 2026-04-27 00:23:33 UTC
# Status: Accepted

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        # street type -> allowed directions
        directions = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }

        seen = set()

        def dfs(r, c):
            if (r, c) == (rows - 1, cols - 1):
                return True

            seen.add((r, c))

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    # neighbor must connect back to current cell
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True

            return False

        return dfs(0, 0)