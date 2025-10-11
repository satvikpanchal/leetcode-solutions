# LeetCode Solution
# Problem: 1603. Running Sum of 1d Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/running-sum-of-1d-array/
# Submitted: 2025-10-11 03:25:22 UTC
# Status: Accepted

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        return prefix