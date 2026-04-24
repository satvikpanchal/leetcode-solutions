# LeetCode Solution
# Problem: 75. Sort Colors
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/sort-colors/
# Submitted: 2026-04-15 19:23:23 UTC
# Status: Accepted

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1

        while i <= r:

            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
