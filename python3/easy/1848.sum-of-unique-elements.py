# LeetCode Solution
# Problem: 1848. Sum of Unique Elements
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/sum-of-unique-elements/
# Submitted: 2025-10-22 00:09:02 UTC
# Status: Accepted

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash_one = {}
        for i in nums:
            if i in hash_one:
                hash_one[i] += 1
            else:
                hash_one[i] = 1

        unique_sum = 0
        for j in hash_one:
            if hash_one[j] == 1:
                unique_sum += j
        
        return unique_sum

        