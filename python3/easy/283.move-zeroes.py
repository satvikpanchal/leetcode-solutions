# LeetCode Solution
# Problem: 283. Move Zeroes
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/move-zeroes/
# Submitted: 2025-10-07 18:38:32 UTC
# Status: Accepted

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while j < len(nums):
            if nums[j] > 0 or nums[j] < 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
