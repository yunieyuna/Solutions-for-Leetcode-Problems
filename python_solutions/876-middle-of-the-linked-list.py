# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        head_copy = head
        while head:
            count += 1
            head = head.next
        
        # even
        if count % 2 == 0:
            count = count / 2
            while count != 0:
                head_copy = head_copy.next
                count -= 1
        # odd
        else:
            count = count // 2
            while count != 0:
                head_copy = head_copy.next
                count -= 1
        return head_copy
            
"""
Runtime: 28 ms, faster than 79.36% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.
"""
