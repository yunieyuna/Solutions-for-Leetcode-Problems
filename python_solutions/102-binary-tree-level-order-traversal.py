# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])
                
            # append the current node value
            levels[level].append(node.val)
            
            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
                
        helper(root, 0)
        return levels

"""
Runtime: 28 ms, faster than 97.12% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.3 MB, less than 82.26% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
