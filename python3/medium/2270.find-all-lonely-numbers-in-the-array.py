# LeetCode Solution
# Problem: 2270. Find All Lonely Numbers in the Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
# Submitted: 2026-01-05 22:43:59 UTC
# Status: Accepted

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dict1 = {}
        result = []

        for i in nums:
            
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for k, v in dict1.items():
            if v == 1:
                if k - 1 not in dict1 and k + 1 not in dict1:
                    result.append(k)
        
        return result