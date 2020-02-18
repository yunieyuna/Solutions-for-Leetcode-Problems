# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        dummy = Node(None, None, head, None)
        self.flatten_dfs(dummy, head)
        
        dummy.next.prev =None
        return dummy.next
    
    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev
        
        curr.prev = prev
        prev.next = curr
        
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)
        
"""
Runtime: 36 ms, faster than 50.06% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
"""
