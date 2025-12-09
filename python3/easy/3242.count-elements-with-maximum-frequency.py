# LeetCode Solution
# Problem: 3242. Count Elements With Maximum Frequency
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Submitted: 2025-10-23 06:12:59 UTC
# Status: Accepted

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_store = {}
        for i in nums:
            if i in hash_store:
                hash_store[i] += 1
            else:
                hash_store[i] = 1

        max_occur = max(hash_store.values())

        total = 0
        for value in hash_store.values():
            if value == max_occur:
                total += value
        
        return total