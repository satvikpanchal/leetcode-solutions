# LeetCode Solution
# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submitted: 2025-10-06 23:42:24 UTC
# Status: Accepted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1