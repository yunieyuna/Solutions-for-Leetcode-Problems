# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMiddle(self, head):
        prevPtr = None
        slowPtr = head
        fastPtr = head
        
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
        if prevPtr:
            prevPtr.next = None
            
        return slowPtr
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        mid = self.findMiddle(head)
        
        node = TreeNode(mid.val)
        
        if head == mid:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
        
"""
Runtime: 136 ms, faster than 35.13% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
"""
