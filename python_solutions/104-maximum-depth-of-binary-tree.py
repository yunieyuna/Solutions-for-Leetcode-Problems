# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ### Thinking Process
        
        ## Method 1： Iterative DFS
        
#         stack = []
#         height = 0
#         max_h = 0
#         while stack or root:
#             while root:
#                 height += 1
#                 stack.append((root, height))
#                 root = root.left
#                 print(stack)
#             root, height = stack.pop()
#             max_h = max(max_h, height)
#             root = root.right
            
#         return max_h
    
        ## Method 2: Recursive DFS
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return 0
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        return max(left_height, right_height) + 1
        
    