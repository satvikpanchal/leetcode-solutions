# LeetCode Solution
# Problem: 2634. Minimum Common Value
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-common-value/
# Submitted: 2025-10-07 18:22:45 UTC
# Status: Accepted

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        cur_small = nums1[0]

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        
        # return cur_small
        return -1