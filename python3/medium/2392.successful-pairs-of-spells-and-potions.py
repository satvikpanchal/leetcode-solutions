# LeetCode Solution
# Problem: 2392. Successful Pairs of Spells and Potions
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Submitted: 2026-04-28 05:28:12 UTC
# Status: Accepted

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        res = []

        for i in spells:
            l, r = 0, len(potions) - 1

            while l <= r:

                middle = (l + r) // 2

                if potions[middle] * i < success:
                    l = middle + 1
                else:
                    r = middle - 1
            
            res.append(len(potions) - l)

        return res