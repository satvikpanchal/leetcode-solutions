# LeetCode Solution
# Problem: 724. Find Pivot Index
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-pivot-index/
# Submitted: 2025-10-12 17:42:04 UTC
# Status: Accepted

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for j in range(1, len(nums)):
            prefix.append(nums[j] + prefix[-1])

        for i in range(0, len(prefix)):
            left = 0 if i == 0 else prefix[i-1]
            if left == prefix[-1] - prefix[i]:
                return i

        return -1 