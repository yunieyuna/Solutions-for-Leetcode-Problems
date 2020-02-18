# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        # add dummy head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return dummy.next
        
"""
Runtime: 72 ms, faster than 46.15% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements.
"""
