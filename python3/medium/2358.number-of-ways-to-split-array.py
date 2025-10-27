# LeetCode Solution
# Problem: 2358. Number of Ways to Split Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-ways-to-split-array/
# Submitted: 2025-10-11 03:20:36 UTC
# Status: Accepted

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for j in range(0, len(nums) - 1):
            valid_sum = prefix[j]
            other_sum = prefix[-1] - prefix[j]

            if valid_sum >= other_sum:
                ans += 1
        
        return ans