# LeetCode Solution
# Problem: 1603. Running Sum of 1d Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/running-sum-of-1d-array/
# Submitted: 2025-09-16 22:58:10 UTC
# Status: Accepted

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        total = 0
        for num in nums:
            total += num
            running.append(total)
        return running