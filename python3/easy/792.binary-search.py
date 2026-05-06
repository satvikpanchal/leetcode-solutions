# LeetCode Solution
# Problem: 792. Binary Search
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/binary-search/
# Submitted: 2026-04-27 23:07:48 UTC
# Status: Accepted

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1