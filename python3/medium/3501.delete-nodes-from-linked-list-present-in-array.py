# LeetCode Solution
# Problem: 3501. Delete Nodes From Linked List Present in Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Submitted: 2025-11-01 20:37:37 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_remove = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        # traverse the linked list
        while curr:
            if curr.val in to_remove:
                # skip the node
                prev.next = curr.next
            else:
                # move prev only if we didn't delete
                prev = curr
            curr = curr.next
        
        return dummy.next