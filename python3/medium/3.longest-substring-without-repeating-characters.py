# LeetCode Solution
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Submitted: 2026-01-07 01:00:26 UTC
# Status: Accepted

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        hash1 = defaultdict(int)

        for r in range(len(s)):
            hash1[s[r]] += 1
            
            while hash1[s[r]] > 1:
                # print(hash1[s[r]])
                hash1[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result



        