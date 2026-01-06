# LeetCode Solution
# Problem: 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Submitted: 2025-12-10 21:58:35 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cur_head = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                rm = cur.next.next
                # print(rm.val)
                cur.next = rm
            # print(cur.val)
            else:
                cur = cur.next

        return head
            
            
        