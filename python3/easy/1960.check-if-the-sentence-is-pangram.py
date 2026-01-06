# LeetCode Solution
# Problem: 1960. Check if the Sentence Is Pangram
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Submitted: 2026-01-05 22:47:47 UTC
# Status: Accepted

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        sentence_set = set(sentence)

        return len(sentence_set) == len(alphabets)