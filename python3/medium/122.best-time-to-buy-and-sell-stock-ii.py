# LeetCode Solution
# Problem: 122. Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Submitted: 2026-05-01 02:25:04 UTC
# Status: Accepted

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                res += prices[r] - prices[l]

            l += 1
            r += 1

        return max(0, res)