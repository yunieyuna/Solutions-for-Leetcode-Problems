# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # ref: https://blog.csdn.net/romeo12334/article/details/81451698
        
        # # method 1: Recursion
        # if not root:
        #     return []
        # if not root.children:
        #     return [root.val]
        # result = [root.val]
        # for child in root.children:
        #     result += self.preorder(child)
        # return result
    
        # method 2: Iteration
        if not root:
            return []
        
        stack = []
        result = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:
                curr.children.reverse()
                stack += curr.children
        return result
        
"""
Runtime: 64 ms, faster than 72.96% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
