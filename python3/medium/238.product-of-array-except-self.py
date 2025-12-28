# LeetCode Solution
# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Submitted: 2025-12-11 23:00:32 UTC
# Status: Accepted

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # prefix
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # suffix and answer
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result