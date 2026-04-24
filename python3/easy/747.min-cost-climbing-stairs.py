# LeetCode Solution
# Problem: 747. Min Cost Climbing Stairs
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/
# Submitted: 2026-04-14 03:22:35 UTC
# Status: Accepted

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(state):
            if state == 0:
                return 0

            if state == 1:
                return 0

            if state in memo:
                return memo[state]

            memo[state] = min(dp(state - 1) + cost[state - 1], dp(state - 2) + cost[state - 2])
            return memo[state]

        memo = {}
        return dp(len(cost))