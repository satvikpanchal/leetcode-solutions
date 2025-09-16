# LeetCode Solution
# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/valid-parentheses/
# Submitted: 2025-07-04 00:05:38 UTC
# Status: Accepted

class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) == 1:
        #     return False
        hash_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in s:
            if i in hash_map:
                if stack and stack[-1] == hash_map[i]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False
        # if stack is None:
        #     return True
        # else:
        #     return False

        # for i in s:
        #     if i == '(' or i == '[' or i == '{':
        #         stack.append(i)
        #     else:
        #         if i == ')':
        #             if stack[-1] == '(':
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif i == ']':
        #             if stack[-1] == '[':
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif i == '}':
        #             if stack[-1] == '{':
        #                 stack.pop()
        #             else:
        #                 return False
        
        # return True