# LeetCode Solution
# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/longest-common-prefix/
# Submitted: 2025-10-30 22:42:20 UTC
# Status: Accepted

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
