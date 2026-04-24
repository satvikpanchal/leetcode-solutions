# LeetCode Solution
# Problem: 215. Kth Largest Element in an Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Submitted: 2026-04-13 03:16:04 UTC
# Status: Accepted

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]