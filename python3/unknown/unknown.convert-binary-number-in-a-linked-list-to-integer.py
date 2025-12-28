# LeetCode Solution
# Problem: unknown. Convert Binary Number in a Linked List to Integer
# Difficulty: Unknown
# Language: Python3
# URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Submitted: 2025-12-13 00:24:23 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        if not head:
            return 0

        binary = ""
        ptr = head

        while ptr:
            binary += str(ptr.val)
            ptr = ptr.next
        
        return int(binary, 2)
        