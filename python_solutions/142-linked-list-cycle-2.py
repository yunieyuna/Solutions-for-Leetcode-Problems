# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        
        ptr1 = head
        ptr2 = intersect
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1
    
    def getIntersect(self, head):
        tortoise = head
        hare = head
        
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise
        
        return None
        
"""
Runtime: 48 ms, faster than 76.62% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
"""
