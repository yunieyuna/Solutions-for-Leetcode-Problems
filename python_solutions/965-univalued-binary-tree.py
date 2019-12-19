# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # method 1: dfs
        vals = []
        
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(set(vals)) == 1

"""
Runtime: 32 ms, faster than 73.24% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Univalued Binary Tree.
"""
