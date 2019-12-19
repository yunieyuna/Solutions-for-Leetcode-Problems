# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # ref: https://blog.csdn.net/fuxuemingzhu/article/details/81017965
        
        # # method 1: Recursion
        # res = []
        # if not root:
        #     return res
        # for child in root.children:
        #     res.extend(self.postorder(child))
        # res.append(root.val)
        # return res
    
        # method 2: Iteration
        res = []
        if not root:
            return res
        stack = [root,]
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            res.append(node.val)
        return res[::-1]

"""
Runtime: 44 ms, faster than 98.42% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
