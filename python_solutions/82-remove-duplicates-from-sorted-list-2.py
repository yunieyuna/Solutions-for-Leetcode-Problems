# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        thead = ListNode('a')
        thead.next = head # 加空头
        pre, cur = None, thead
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
                pre.next = cur
        return thead.next
        
"""
Runtime: 88 ms, faster than 7.85% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
