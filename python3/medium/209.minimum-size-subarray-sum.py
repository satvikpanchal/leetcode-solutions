# LeetCode Solution
# Problem: 209. Minimum Size Subarray Sum
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-size-subarray-sum/
# Submitted: 2025-10-08 06:23:40 UTC
# Status: Accepted

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = cur = 0
        ans = float('inf')

        for r in range(0, len(nums)):
            
            cur += nums[r]

            while cur >= target:
                ans = min(ans, r - l + 1)
                cur -= nums[l]
                l += 1
        
        return ans if ans != float('inf') else 0