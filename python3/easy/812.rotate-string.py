# LeetCode Solution
# Problem: 812. Rotate String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/rotate-string/
# Submitted: 2026-05-03 17:18:45 UTC
# Status: Accepted

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        r = 0

        while r < len(s):
            
            if s[r + 1:] + s[0:r + 1] == goal:
                
                return True

            r += 1
        
        return False