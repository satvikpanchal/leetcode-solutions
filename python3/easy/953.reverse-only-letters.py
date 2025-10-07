# LeetCode Solution
# Problem: 953. Reverse Only Letters
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-only-letters/
# Submitted: 2025-10-07 18:08:51 UTC
# Status: Accepted

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s) - 1
        string_s = list(s)

        print(string_s)

        while i < j:
            while not string_s[i].isalpha() and i < j:
                i += 1
            
            while not string_s[j].isalpha() and i < j:
                j -= 1
                
            string_s[i], string_s[j] = string_s[j], string_s[i]
        
            i += 1
            j -= 1

        return ''.join(string_s)