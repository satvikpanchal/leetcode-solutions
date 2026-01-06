# LeetCode Solution
# Problem: 2427. First Letter to Appear Twice
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/first-letter-to-appear-twice/
# Submitted: 2026-01-05 22:20:30 UTC
# Status: Accepted

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_hash = {}
        for i in s:
            if i in letter_hash:
                return i
            letter_hash[i] = 1