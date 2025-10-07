# LeetCode Solution
# Problem: 392. Is Subsequence
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/is-subsequence/
# Submitted: 2025-10-07 00:08:40 UTC
# Status: Accepted

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1 
            j += 1
        
        return i == len(s)
