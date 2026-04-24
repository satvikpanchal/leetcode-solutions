# LeetCode Solution
# Problem: 1126. Minimum Cost to Connect Sticks
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# Submitted: 2026-04-13 03:14:07 UTC
# Status: Accepted

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # heap = []
        heapq.heapify(sticks)
        res = 0
        
        while len(sticks) > 1:
            one = heapq.heappop(sticks)
            two = heapq.heappop(sticks)
            addition = one + two
            res += addition
            heapq.heappush(sticks, addition)

        return res