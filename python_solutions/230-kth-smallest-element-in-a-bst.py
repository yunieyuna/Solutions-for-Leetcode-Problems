# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        res = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return 0
        
"""
Runtime: 44 ms, faster than 96.61% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 16.7 MB, less than 98.18% of Python3 online submissions for Kth Smallest Element in a BST.
"""
