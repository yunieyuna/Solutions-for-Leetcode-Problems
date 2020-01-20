# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail: (n - k % n - 1)th node
        # find new head: (n - k % n)th node
        new_tail = head
        for i in range(n - k%n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head
        
"""
时间复杂度：O(N)O(N)，其中 NN 是链表中的元素个数
空间复杂度：O(1)O(1)，因为只需要常数的空间
"""
