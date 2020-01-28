# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        # one of node is None
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
Runtime: 32 ms, faster than 32.31% of Python3 online submissions for Same Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Same Tree.
"""
