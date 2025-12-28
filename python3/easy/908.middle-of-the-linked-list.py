# LeetCode Solution
# Problem: 908. Middle of the Linked List
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/middle-of-the-linked-list/
# Submitted: 2025-12-10 21:35:06 UTC
# Status: Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast  = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            # if fast != None and fast.next != None:
            fast = fast.next.next
            # print(slow.val)
            # print(fast.val)
            # print(...)

        return slow


        # count = 0
        # head1 = head
        # head2 = head
        
        # while head1:
        #     count += 1
        #     head1 = head1.next
        
        # middle = math.ceil(count / 2)
        # print(middle)
        
        # even_odd = False
        # if count % 2 == 1:
        #     even_odd = False
        # else:
        #     even_odd = True
        
        # while middle > 1:
        #     head2 = head2.next
        #     middle -= 1
            
        # if even_odd == True:
        #     return head2.next
        # else:
        #     return head2
                
            
        