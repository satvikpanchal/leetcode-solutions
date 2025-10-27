# LeetCode Solution
# Problem: 1098. Largest Unique Number
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/largest-unique-number/
# Submitted: 2025-10-19 18:52:03 UTC
# Status: Accepted

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hash_map = {}
        
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
            
        one_occur = []
        for j in hash_map:
            if hash_map[j] == 1:
                one_occur.append(j)
            
                
        return max(one_occur) if len(one_occur) > 0 else -1