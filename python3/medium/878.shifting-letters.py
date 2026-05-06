# LeetCode Solution
# Problem: 878. Shifting Letters
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/shifting-letters/
# Submitted: 2026-05-05 23:22:29 UTC
# Status: Accepted

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        total = 0
        res = ""

        for i in range(len(shifts) - 1, -1, -1):
            total += shifts[i]
            shifts[i] = total
        
        for i in range(0, len(s)):
            ascii_val = (ord(s[i]) - ord('a') + shifts[i]) % 26
            res += chr(ascii_val + ord('a'))

        return res
