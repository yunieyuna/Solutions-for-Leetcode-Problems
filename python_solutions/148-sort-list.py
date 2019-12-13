# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # cut the Linked List at the mid index
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        
        # recursive for cutting
        left, right = self.sortList(head), self.sortList(mid)
        
        # merge left and right linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next
                
"""
Runtime: 216 ms, faster than 77.10% of Python3 online submissions for Sort List.
Memory Usage: 19.6 MB, less than 100.00% of Python3 online submissions for Sort List.
"""
