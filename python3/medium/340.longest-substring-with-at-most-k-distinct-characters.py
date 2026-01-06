# LeetCode Solution
# Problem: 340. Longest Substring with At Most K Distinct Characters
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Submitted: 2026-01-05 23:57:27 UTC
# Status: Accepted

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        best = 0
        l = 0
        temp_hash = defaultdict(int)

        for r in range(len(s)):
            temp_hash[s[r]] += 1
            # result += 1

            while len(temp_hash) > k:
                temp_hash[s[l]] -= 1
                if temp_hash[s[l]] == 0:
                    del temp_hash[s[l]]

                # result -= 1
                l += 1
        
            best = max(best, r - l + 1)

        return best


