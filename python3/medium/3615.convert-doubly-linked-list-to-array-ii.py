# LeetCode Solution
# Problem: 3615. Convert Doubly Linked List to Array II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/
# Submitted: 2025-12-13 00:51:05 UTC
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
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        result = []
        ptr = node

        while ptr.prev:
            ptr = ptr.prev
        
        print(ptr.val)
        left_to_right_ptr = ptr
        while left_to_right_ptr:
            result.append(left_to_right_ptr.val)
            left_to_right_ptr = left_to_right_ptr.next

        return result
        