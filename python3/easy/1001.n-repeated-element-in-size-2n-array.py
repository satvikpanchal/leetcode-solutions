# LeetCode Solution
# Problem: 1001. N-Repeated Element in Size 2N Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Submitted: 2026-05-05 01:01:16 UTC
# Status: Accepted

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for i in nums:
            if i in hashmap:
                return i
            
            hashmap[i] += 1
        
        return -1