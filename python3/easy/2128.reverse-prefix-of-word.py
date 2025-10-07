# LeetCode Solution
# Problem: 2128. Reverse Prefix of Word
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-prefix-of-word/
# Submitted: 2025-10-07 20:08:52 UTC
# Status: Accepted

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = j = 0
        new_word = list(word)

        while j < len(new_word):
            if new_word[j] == ch:
                new_word[i:j+1] = new_word[i:j+1][::-1]
                return ''.join(new_word)
            j += 1

        return ''.join(new_word)