# LeetCode Solution
# Problem: 1960. Check if the Sentence Is Pangram
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Submitted: 2025-10-16 02:59:32 UTC
# Status: Accepted

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        sentence_set = set(sentence)
        # hash = {}
        # for i in sentence_set:
        #     if i not in hash:
        #         hash[i] = 1

        return len(sentence_set) == len(alphabets)