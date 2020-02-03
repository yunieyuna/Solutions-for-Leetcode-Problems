# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # DFS
        self.res = 0
        
        def helper(root, tmp):
            if not root:
                return
            if not root.left and not root.right:
                self.res += int(tmp + str(root.val))
                return
            helper(root.left, tmp+str(root.val))
            helper(root.right, tmp+str(root.val))
        helper(root, "")
        return self.res
        
"""
Runtime: 20 ms, faster than 99.28% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum Root to Leaf Numbers.
"""
