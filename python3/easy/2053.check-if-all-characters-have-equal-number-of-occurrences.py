# LeetCode Solution
# Problem: 2053. Check if All Characters Have Equal Number of Occurrences
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# Submitted: 2026-01-07 00:11:49 UTC
# Status: Accepted

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash1 = defaultdict(int)
        
        for i in s:
            hash1[i] += 1 
        
        occur = set()
        for j in hash1:
            occur.add(hash1[j])
        
        return len(occur) == 1
