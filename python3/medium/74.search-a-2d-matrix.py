# LeetCode Solution
# Problem: 74. Search a 2D Matrix
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/search-a-2d-matrix/
# Submitted: 2026-04-27 23:54:19 UTC
# Status: Accepted

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, (n * m) - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // m
            col = mid % m
            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1

        return False