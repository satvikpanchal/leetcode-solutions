# LeetCode Solution
# Problem: 1321. Get Equal Substrings Within Budget
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/get-equal-substrings-within-budget/
# Submitted: 2025-10-11 22:15:14 UTC
# Status: Accepted

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        cost = maxCost
        ans = 0

        for r in range(0, len(s)):
            diff = ord(s[r]) - ord(t[r])

            if abs(diff) > 0:
                cost -= abs(diff)

            while cost < 0:
                l_diff = ord(s[l]) - ord(t[l])
                cost += abs(l_diff)
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans