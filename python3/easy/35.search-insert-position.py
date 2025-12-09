# LeetCode Solution
# Problem: 35. Search Insert Position
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/search-insert-position/
# Submitted: 2025-10-27 04:41:14 UTC
# Status: Accepted

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If not found, left is the correct insert position
        return left
