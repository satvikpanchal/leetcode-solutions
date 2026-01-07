# LeetCode Solution
# Problem: 383. Ransom Note
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/ransom-note/
# Submitted: 2026-01-07 00:43:30 UTC
# Status: Accepted

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        need = ransomNote
        have = defaultdict(int)

        for i in magazine:
            have[i] += 1

        print(have)

        for j in need:
            print(j)
            if have[j]:
                have[j] -= 1
            elif have[j] <= 0:
                return False

        return True

        