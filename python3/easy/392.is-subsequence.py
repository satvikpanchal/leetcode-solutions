# LeetCode Solution
# Problem: 392. Is Subsequence
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/is-subsequence/
# Submitted: 2025-09-02 07:23:26 UTC
# Status: Accepted

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # subs_list = list(s)
        # t_list = list(t)
        # l = 0

        # for r in range(0, len(t_list)):
        #     while(t_list[r] not in subs_list):
        #         filtered = [ch for ch in t_list if ch in subs_list]

        # print(filtered)

        # subs_list = list(s)
        # t_list = list(t)
        # filtered = [ch for ch in t_list if ch in subs_list]
        # print(subs_list)
        # print(filtered)
        # return filtered == subs_list if len(filtered) == len(subs_list) else False

        # subs_list = list(s)
        # t_list = list(t)

        # start = 0
        # for i in t_list:
        #     if i == subs_list[start]:


        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == len(s):
            return True
        else:
            return False


