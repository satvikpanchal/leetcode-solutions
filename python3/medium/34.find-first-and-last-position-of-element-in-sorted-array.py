# LeetCode Solution
# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Submitted: 2026-05-02 23:09:15 UTC
# Status: Accepted

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid
                    r = mid - 1   # keep searching left
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return ans

        def findLast():
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid
                    l = mid + 1   # keep searching right
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return ans

        return [findFirst(), findLast()]
        