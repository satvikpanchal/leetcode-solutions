# LeetCode Solution
# Problem: unknown. Unique Number of Occurrences
# Difficulty: Unknown
# Language: Python3
# URL: https://leetcode.com/problems/unique-number-of-occurrences/
# Submitted: 2025-10-24 22:02:25 UTC
# Status: Accepted

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dicti = {}
        for i in arr:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1
        
        return True if len(set(arr)) == len(set(dicti.values())) else False