# LeetCode Solution
# Problem: 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Submitted: 2025-07-16 03:29:01 UTC
# Status: Accepted

# Half
# compare left and right
# half whichever smaller


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]

        