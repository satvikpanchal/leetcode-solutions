# LeetCode Solution
# Problem: 203. Remove Linked List Elements
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/remove-linked-list-elements/
# Submitted: 2025-12-13 00:37:06 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur          
            cur = cur.next          

        return dummy.next
        