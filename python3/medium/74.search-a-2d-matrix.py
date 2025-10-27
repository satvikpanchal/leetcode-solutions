# LeetCode Solution
# Problem: 74. Search a 2D Matrix
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/search-a-2d-matrix/
# Submitted: 2025-10-27 04:38:39 UTC
# Status: Accepted

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            r, c = divmod(mid, n)      # r = mid // n, c = mid % n
            val = matrix[r][c]
            
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False