# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 哑节点
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
                
            head = head.next
            
        after.next = None
        before.next = after_head.next
        
        return before_head.next
        
"""
Runtime: 28 ms, faster than 89.42% of Python3 online submissions for Partition List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Partition List.
"""
