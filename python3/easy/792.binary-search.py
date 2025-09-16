# LeetCode Solution
# Problem: 792. Binary Search
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/binary-search/
# Submitted: 2025-07-05 02:26:26 UTC
# Status: Accepted

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = (l + r) // 2

            if nums[midpoint] > target:
                r = midpoint - 1
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                return midpoint

        return -1
        