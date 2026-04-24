# LeetCode Solution
# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/climbing-stairs/
# Submitted: 2026-04-14 03:36:56 UTC
# Status: Accepted

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(i):
            if i == 0:
                return 1
            
            if i == 1:
                return 1

            if i in memo:
                return memo[i]

            memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]

        memo = {}
        return dp(n)
        