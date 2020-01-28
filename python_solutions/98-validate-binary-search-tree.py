# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            
            return True
        
        return helper(root)
        
"""
Runtime: 44 ms, faster than 63.83% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
"""
