# LeetCode Solution
# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/valid-palindrome/
# Submitted: 2025-07-02 00:53:54 UTC
# Status: Accepted

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNumeric(s[left]):
                left += 1
            while left < right and not self.alphaNumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
        
    def alphaNumeric(self, s):
        return ((ord('a') <= ord(s) <= ord('z'))
                or (ord('A') <= ord(s) <= ord('Z'))
                or (ord('0') <= ord(s) <= ord('9')))