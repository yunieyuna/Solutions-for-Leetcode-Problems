# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        def helper(root, tmp, sum_):
            if not root:
                return 
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)
        res = []
        helper(root, [], sum_)
        return res

"""
Runtime: 52 ms, faster than 25.20% of Python3 online submissions for Path Sum II.
Memory Usage: 17.7 MB, less than 37.93% of Python3 online submissions for Path Sum II.
"""
