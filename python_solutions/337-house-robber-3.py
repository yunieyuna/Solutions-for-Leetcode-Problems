# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))
    
    def dp(self, cur: TreeNode) -> List[int]:
        if not cur:
            return [0,0]
        
        l = self.dp(cur.left)
        r = self.dp(cur.right)
        
        return [max(l) + max(r), cur.val + l[0] + r[0]]
             
"""
Runtime: 36 ms, faster than 99.48% of Python3 online submissions for House Robber III.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for House Robber III.
"""
