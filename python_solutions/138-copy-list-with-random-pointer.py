# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visitedHash = {}
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        # if we have already processed the current node,
        # then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)
        
        # save this value in the hash map
        self.visitedHash[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
        
"""
Runtime: 32 ms, faster than 83.55% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
"""
