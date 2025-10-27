# LeetCode Solution
# Problem: 1046. Max Consecutive Ones III
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/max-consecutive-ones-iii/
# Submitted: 2025-10-10 06:04:44 UTC
# Status: Accepted

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = cur = ans = 0
        
        for r in range(0, len(nums)):
            
            if nums[r] == 0:
                cur += 1
                
            while cur > k:
                if nums[l] == 0:
                    cur -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
            
        
        return ans
                