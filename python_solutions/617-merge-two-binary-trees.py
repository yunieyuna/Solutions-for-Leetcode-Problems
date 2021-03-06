# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        ### How to crack
        
        ## Method 1: add one tree to another
        if not t1 and not t2: return 
        if not t1 and t2: return t2
        if not t2 and t1: return t1

        t1.val=t1.val+t2.val
        t1.left=self.mergeTrees(t1.left, t2.left)
        t1.right=self.mergeTrees(t1.right, t2.right)
        return t1