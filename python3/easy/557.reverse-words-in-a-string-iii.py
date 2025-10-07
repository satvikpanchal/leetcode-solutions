# LeetCode Solution
# Problem: 557. Reverse Words in a String III
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Submitted: 2025-10-07 05:29:59 UTC
# Status: Accepted

class Solution:
    def reverseWords(self, s: str) -> str:
        i = j = 0
        reversed_sentence = []
        end = 0

        while j < len(s):
            if s[j] == " " or j == len(s) - 1:
                if s[j] == " ":
                    reversed_sentence.append(s[i:j][::-1])
                else:
                    reversed_sentence.append(s[i:j+1][::-1])
                i = j + 1
            j += 1

        return(" ".join(reversed_sentence))