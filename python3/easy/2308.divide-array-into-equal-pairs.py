# LeetCode Solution
# Problem: 2308. Divide Array Into Equal Pairs
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/divide-array-into-equal-pairs/
# Submitted: 2025-09-10 05:42:11 UTC
# Status: Accepted

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        pairs = 0
        for k, v in counter.items():
            if v % 2 == 1:
                return False

        return True
