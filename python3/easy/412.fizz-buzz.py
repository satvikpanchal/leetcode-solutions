# LeetCode Solution
# Problem: 412. Fizz Buzz
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/fizz-buzz/
# Submitted: 2025-09-15 01:26:38 UTC
# Status: Accepted

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz_list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_buzz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_buzz_list.append("Fizz")
            elif i % 5 == 0:
                fizz_buzz_list.append("Buzz")
            else:
                fizz_buzz_list.append(str(i))

        return fizz_buzz_list

        