# LeetCode Solution
# Problem: 19. Remove Nth Node From End of List
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Submitted: 2025-12-10 22:22:53 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, head

        count = n

        while count > 0 and r:
            r = r.next
            count -= 1
        
        while r:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next

        