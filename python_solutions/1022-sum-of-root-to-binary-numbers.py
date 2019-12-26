# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(node):
            if not node.left and not node.right:
                return [str(node.val)]

            left, right = [], []
            if node.left:
                left = [str(node.val) + x for x in traverse(node.left)]
            if node.right:
                right = [str(node.val) + x for x in traverse(node.right)]
                
            return left + right
        
        return sum([int(x, 2) for x in traverse(root)])
        
"""
Runtime: 40 ms, faster than 60.87% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
"""
