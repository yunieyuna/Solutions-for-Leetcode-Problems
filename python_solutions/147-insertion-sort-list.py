# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        
        while cur.next:
            if cur.val > cur.next.val:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next 
                
                m = cur.next
                cur.next = m.next
                m.next = pre.next
                pre.next = m
            else:
                cur = cur.next
                
        return dummy.next
        
"""
Runtime: 216 ms, faster than 61.23% of Python3 online submissions for Insertion Sort List.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Insertion Sort List.
"""
