# LeetCode Solution
# Problem: unknown. Maximum Average Subarray I
# Difficulty: Unknown
# Language: Python3
# URL: https://leetcode.com/problems/maximum-average-subarray-i/
# Submitted: 2025-10-10 05:57:41 UTC
# Status: Accepted

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = ans = 0
        for i in range(k):
            cur += nums[i]
            
        ans = (cur / k)
        for j in range(k, len(nums)):
            cur += nums[j] - nums[j - k]
            
            ans = max(ans, (cur/k))
            
        
        return ans
            