# LeetCode Solution
# Problem: 73. Set Matrix Zeroes
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/set-matrix-zeroes/
# Submitted: 2026-04-29 23:27:04 UTC
# Status: Accepted

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        seen = set()

        for r in range(0, row):
            for c in range(0, col):
                
                if matrix[r][c] == 0:
                    seen.add((r, c))

        for r, c in seen:
            matrix[r][:] = [0] * col

            for i in range(row):
                matrix[i][c] = 0

        
