# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        n1, n2, n3 = head, head.next, head.next
        
        while n1 and n1.next and n2 and n2.next:
            n1.next = n1.next.next
            n1 = n1.next
            n2.next = n2.next.next
            n2 = n2.next
        n1.next = n3
        return head
            
"""
Runtime: 44 ms, faster than 51.28% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.
"""
