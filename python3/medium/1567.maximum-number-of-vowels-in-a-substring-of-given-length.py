# LeetCode Solution
# Problem: 1567. Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Submitted: 2025-10-10 06:23:35 UTC
# Status: Accepted

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        for i in range(k, len(s)):
            if s[i] in vowels:       
                count += 1
            if s[i - k] in vowels:   
                count -= 1
            ans = max(ans, count)

        return ans
