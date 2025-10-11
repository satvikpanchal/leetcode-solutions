# LeetCode Solution
# Problem: 2211. K Radius Subarray Averages
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/k-radius-subarray-averages/
# Submitted: 2025-10-11 21:34:22 UTC
# Status: Accepted

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for j in range(1, len(nums)):
            prefix.append(nums[j] + prefix[-1])

        sub_array_avg = list()
        for i in range(0, len(nums)):
            if i < k or i + k >= len(nums):
                sub_array_avg.append(-1)
            else:
                l, r = i - k, i + k
                if l == 0:
                    window_sum = prefix[r]
                else:
                    window_sum = prefix[r] - prefix[l - 1]

                sub_array_avg.append(window_sum // (2 * k + 1))

        return sub_array_avg