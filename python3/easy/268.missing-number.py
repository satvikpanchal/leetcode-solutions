# LeetCode Solution
# Problem: 268. Missing Number
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/missing-number/
# Submitted: 2026-01-05 22:57:34 UTC
# Status: Accepted

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        nums_set = set(nums)

        for i in nums:
            if start in nums_set:
                pass
            else:
                return start
            start += 1
        
        return len(nums)