# LeetCode Solution
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/group-anagrams/
# Submitted: 2025-06-18 03:19:44 UTC
# Status: Accepted

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for chars in word:
                count[ord(chars) - ord("a")] += 1

            result[tuple(count)].append(word)

        return list(result.values())
