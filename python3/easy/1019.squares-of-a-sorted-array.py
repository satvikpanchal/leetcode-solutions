# LeetCode Solution
# Problem: 1019. Squares of a Sorted Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/squares-of-a-sorted-array/
# Submitted: 2025-10-07 04:47:42 UTC
# Status: Accepted

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        end_index = len(nums) - 1
        sorted_list = [0] * len(nums)

        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                sorted_list[end_index] = nums[i] ** 2
                i += 1
            else:
                sorted_list[end_index] = nums[j] ** 2
                j -= 1

            end_index -= 1

        return sorted_list