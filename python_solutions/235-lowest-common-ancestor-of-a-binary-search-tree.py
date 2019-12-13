# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/# 
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # value of current node or parent node
        parent_val = root.val
        
        # value of p
        p_val = p.val
        
        # value of q
        q_val = q.val
        
        # if both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # if both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return root

"""
Runtime: 68 ms, faster than 99.45% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""
