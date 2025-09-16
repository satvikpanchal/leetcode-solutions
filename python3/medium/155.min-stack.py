# LeetCode Solution
# Problem: 155. Min Stack
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/min-stack/
# Submitted: 2025-07-04 00:24:19 UTC
# Status: Accepted

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_val = val
        if len(self.minStack) > 0:
            min_val = min(self.minStack[-1], min_val)
        else:
            min_val = val

        self.minStack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()