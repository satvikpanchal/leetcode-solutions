# LeetCode Solution
# Problem: 3581. The Two Sneaky Numbers of Digitville
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
# Submitted: 2025-10-31 21:06:56 UTC
# Status: Accepted

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash_track = {}
        freq_nums = set()

        for i in nums:
            if i in hash_track:
                freq_nums.add(i)
            else:
                hash_track[i] = 1

        return list(freq_nums)