# LeetCode Solution
# Problem: 344. Reverse String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-string/
# Submitted: 2025-09-12 03:59:11 UTC
# Status: Accepted

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        