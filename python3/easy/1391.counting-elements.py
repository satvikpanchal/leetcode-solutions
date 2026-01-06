# LeetCode Solution
# Problem: 1391. Counting Elements
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/counting-elements/
# Submitted: 2026-01-05 22:59:49 UTC
# Status: Accepted

class Solution:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        arr_set = set(arr)
        
        for i in arr:
            if i + 1 in arr_set:
                result += 1
        return result