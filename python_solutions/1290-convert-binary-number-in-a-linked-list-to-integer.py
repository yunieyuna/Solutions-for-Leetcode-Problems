# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_value_list = '0b'
        while head:
            binary_value_list += str(head.val)
            head = head.next
        return int(binary_value_list, 2)
        
"""
Runtime: 16 ms, faster than 99.71% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
