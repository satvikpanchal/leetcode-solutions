# LeetCode Solution
# Problem: 149. Max Points on a Line
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/max-points-on-a-line/
# Submitted: 2025-09-27 00:21:54 UTC
# Status: Accepted

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1

        for i in range(0, len(points)):
            slope_dict = {}
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0]:
                    slope = float("inf")
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                if slope in slope_dict:
                    slope_dict[slope] += 1
                else:
                    slope_dict[slope] = 1

                result = max(result, slope_dict[slope] + 1)

        return result