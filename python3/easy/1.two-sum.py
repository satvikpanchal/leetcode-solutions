# LeetCode Solution
# Problem: 1. Two Sum
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/two-sum/
# Submitted: 2025-10-06 23:38:13 UTC
# Status: Accepted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_track = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]

            if diff in index_track:
                return [index_track[diff], i]
            else:
                index_track[nums[i]] = i