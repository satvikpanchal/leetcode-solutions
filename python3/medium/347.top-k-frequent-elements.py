# LeetCode Solution
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submitted: 2025-06-20 04:42:35 UTC
# Status: Accepted

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_list = nums
        freq_dict = {}

        for i in sorted_list:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        sorted_values = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

        final_list = []

        for i in sorted_values[0:k]:
            final_list.append(i[0])


        return final_list
        