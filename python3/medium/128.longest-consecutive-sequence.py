# LeetCode Solution
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Submitted: 2026-04-16 00:01:56 UTC
# Status: Accepted

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        ans = 1

        for i in s:
            r = i + 1

            if i - 1 not in s:
                while r in s:
                    ans += 1
                    r += 1

            res = max(res, ans)
            ans = 1

        return res
