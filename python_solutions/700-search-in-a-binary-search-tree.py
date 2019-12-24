# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1: recursion
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            pass
        else:
            if root.val == val:
                return root
            elif root.val > val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)
        
        return None
        
"""
Runtime: 68 ms, faster than 97.25% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Search in a Binary Search Tree.
"""



# method 2: iteration
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp == None:
                continue
            if tmp.val == val:
                return tmp
            else:
                stack.append(tmp.left)
                stack.append(tmp.right)
        return None
        
"""
Runtime: 76 ms, faster than 78.42% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Search in a Binary Search Tree.
"""



# method 3: 因为是BST，所以可以直接遍历
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val== val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
        
"""
Runtime: 76 ms, faster than 78.42% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Search in a Binary Search Tree.
"""
