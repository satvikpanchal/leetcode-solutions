# LeetCode Solution
# Problem: 303. Range Sum Query - Immutable
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/range-sum-query-immutable/
# Submitted: 2025-10-13 18:29:52 UTC
# Status: Accepted

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix = [self.nums[0]]

        for i in range(1, len(self.nums)):
            prefix.append(self.nums[i] + prefix[-1])

        if left == 0:
            return prefix[right]
        else:
            return prefix[right] - prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)