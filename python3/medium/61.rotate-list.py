# LeetCode Solution
# Problem: 61. Rotate List
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/rotate-list/
# Submitted: 2026-05-05 00:58:57 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        
        ptr = head
        length = 0

        while ptr != None:
            length += 1
            ptr = ptr.next
        
        k %= length
        if k == 0:
            return head
        
        if k == 0:
            return head
        
        # now the logic of rotation
        first = head
        second = head
        counter = 0

        while counter != length - k - 1:
            first = first.next
            counter += 1

        new_head = first.next

        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head
        first.next = None

        return new_head
        
