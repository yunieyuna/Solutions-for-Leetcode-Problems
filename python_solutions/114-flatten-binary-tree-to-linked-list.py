# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while (root != None):
            if root.left != None:
                most_right = root.left
                while most_right.right != None:
                    most_right = most_right.right
                most_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return
        
"""
Runtime: 36 ms, faster than 83.33% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""
