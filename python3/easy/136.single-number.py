# LeetCode Solution
# Problem: 136. Single Number
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/single-number/
# Submitted: 2025-09-19 05:39:59 UTC
# Status: Accepted

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dict = Counter(nums)
        for i, j in freq_dict.items():
            if j == 1:
                return i
        