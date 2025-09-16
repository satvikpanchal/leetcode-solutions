# LeetCode Solution
# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submitted: 2025-07-02 21:45:23 UTC
# Status: Accepted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        two_sum = 0

        while l < r:
            two_sum = numbers[l] + numbers[r]

            if two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


            