# LeetCode Solution
# Problem: 3577. Convert Doubly Linked List to Array I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/
# Submitted: 2025-12-13 00:39:02 UTC
# Status: Accepted

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        result = []
        ptr = root
        while ptr:
            result.append(ptr.val)
            ptr = ptr.next
        return result

        