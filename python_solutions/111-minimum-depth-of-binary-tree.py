# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        children = [root.left, root.right]
        
        if not any(children):
            return 1
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        
        return min_depth + 1
        
"""
Runtime: 52 ms, faster than 16.73% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 14.6 MB, less than 62.16% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
