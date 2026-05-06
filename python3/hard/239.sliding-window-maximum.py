# LeetCode Solution
# Problem: 239. Sliding Window Maximum
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/sliding-window-maximum/
# Submitted: 2026-05-05 01:43:14 UTC
# Status: Accepted

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for idx, i in enumerate(nums):
            heapq.heappush(heap, (-i, idx))

            while heap[0][1] < idx - k + 1:
                heapq.heappop(heap)
            
            if idx >= k - 1:
                res.append(-heap[0][0])
        
        return res
            




