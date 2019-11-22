# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longest = 1
        
        def depth(root):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            
            # update longest
            # for each root, the longest path will be L + R + 1
            self.longest = max(self.longest, L + R + 1)
            
            # while for passing through one root, only need the longest root, either left or right.
            return 1 + max(L, R)
        
        depth(root)
        return self.longest - 1