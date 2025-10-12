# LeetCode Solution
# Problem: 1833. Find the Highest Altitude
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-the-highest-altitude/
# Submitted: 2025-10-12 17:30:52 UTC
# Status: Accepted

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [gain[0]]
        for i in range(1, len(gain)):
            prefix.append(gain[i] + prefix[-1])

        max_point = max(prefix)
        return max_point if max_point > 0 else 0