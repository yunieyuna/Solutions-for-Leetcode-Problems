# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 , s2 = 0, 0
        while l1:
            s1 = s1*10 + l1.val
            l1 = l1.next
        while l2:
            s2 = s2*10 + l2.val
            l2 = l2.next
        s = s1 + s2
        
        head = ListNode(0)
        if s == 0:
            return head
        
        while s:
            v, s = s%10, s//10
            head.next, head.next.next = ListNode(v), head.next
            
        return head.next
        
"""
Runtime: 72 ms, faster than 69.52% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.
"""
