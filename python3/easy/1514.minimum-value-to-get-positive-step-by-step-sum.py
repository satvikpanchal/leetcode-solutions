# LeetCode Solution
# Problem: 1514. Minimum Value to Get Positive Step by Step Sum
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# Submitted: 2025-10-12 17:24:55 UTC
# Status: Accepted

class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        min_start = 1
        total_sum = 1

        for i in nums:
            # [-3,2,-3,4,2]
            total_sum += i  # -3 + -1 = -4
            # total_sum += min_start

            if total_sum <= 0:
                min_start += abs(total_sum) + 1 # 4
                total_sum = 1

        return min_start