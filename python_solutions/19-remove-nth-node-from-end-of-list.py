# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        dummy = ListNode(0)
        dummy.next = head
        first_pointer = dummy
        second_pointer = dummy
        
        for i in range(n+1):
            first_pointer = first_pointer.next
            
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        
        second_pointer.next = second_pointer.next.next

        return dummy.next
        
"""
Runtime: 32 ms, faster than 51.88% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
"""
