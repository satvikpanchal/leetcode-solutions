# LeetCode Solution
# Problem: 1293. Three Consecutive Odds
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/three-consecutive-odds/
# Submitted: 2025-10-05 01:15:27 UTC
# Status: Accepted

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            if i + 2 < len(arr):
                if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                    return True
        return False