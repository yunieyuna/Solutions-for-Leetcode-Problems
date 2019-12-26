# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findleaf(root1) == self.findleaf(root2)
    
    def findleaf(self, root):
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)
        
"""
Runtime: 36 ms, faster than 55.00% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Leaf-Similar Trees.
"""
