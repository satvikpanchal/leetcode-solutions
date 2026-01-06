# LeetCode Solution
# Problem: 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Submitted: 2025-11-04 04:56:57 UTC
# Status: Accepted

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        l, r = 0, 0
        while r < len(haystack):

            if haystack[l:r+1] == needle:
                print(haystack[l:r+1], l)
                return l

            if len(haystack[l:r + 1]) >= len(needle):
                l += 1
            
            r += 1

        return index
        