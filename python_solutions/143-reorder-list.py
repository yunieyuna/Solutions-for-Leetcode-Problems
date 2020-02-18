# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        p = head
        stack = []
        while p:
            stack.append(p)
            p = p.next
        
        n = len(stack)
        count = (n-1) // 2 # 中点前一个位置
        p = head
        while count:
            tmp = stack.pop()
            tmp.next = p.next
            p.next = tmp
            p = tmp.next
            count -= 1
        
        stack.pop().next = None
            
            
"""
Runtime: 80 ms, faster than 98.20% of Python3 online submissions for Reorder List.
Memory Usage: 22 MB, less than 15.38% of Python3 online submissions for Reorder List.
"""
