# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # method 1: Recursion
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            print(height)
            return max(height) + 1
            
"""
Runtime: 48 ms, faster than 83.58% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""
