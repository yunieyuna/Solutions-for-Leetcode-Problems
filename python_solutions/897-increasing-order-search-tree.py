# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        array = self.in_order(root)
        if not array:
            return None
        newRoot = TreeNode(array[0])
        curr = newRoot
        for i in range(1, len(array)):
            curr.right = TreeNode(array[i])
            curr = curr.right
        return newRoot
    
    def in_order(self, root):
        if not root:
            return []
        array = []
        array.extend(self.in_order(root.left))
        array.append(root.val)
        array.extend(self.in_order(root.right))
        return array
        
"""
Runtime: 96 ms, faster than 51.35% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Increasing Order Search Tree.
"""
