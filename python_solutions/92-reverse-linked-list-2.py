# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        left, right = head, head
        stop = False
        
        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            
            # base case, don't proceed any further
            if n == 1:
                return
            
            right = right.next
            
            if m > 1:
                left = left.next
                
            recurseAndReverse(right, m - 1, n - 1)
            
            if left == right or right.next == left:
                stop = True
                
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
                
        recurseAndReverse(right, m, n)
        return head
        
"""
Runtime: 32 ms, faster than 36.69% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13.1 MB, less than 77.78% of Python3 online submissions for Reverse Linked List II.
"""
