# LeetCode Solution
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/container-with-most-water/
# Submitted: 2025-07-02 01:13:13 UTC
# Status: Accepted

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1

        while l < r:

            area = (r - l) * min(height[l], height[r])
            result = max(result, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result
        