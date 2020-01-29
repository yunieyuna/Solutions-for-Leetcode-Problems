# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1
    
    def depth(self, root):
        if not root:
            return 0
        
        left = self.depth(root.left)
        if left == -1:
            return -1
        
        right = self.depth(root.right)
        if right == -1:
            return -1
        
        return max(left, right) + 1 if abs(left - right) < 2 else -1
        
"""
Runtime: 40 ms, faster than 97.77% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Balanced Binary Tree.
"""
