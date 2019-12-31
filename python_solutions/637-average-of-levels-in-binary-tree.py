# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        
        result = []
        current_level = [root]
        while current_level:
            level_nodes = []
            next_level = []
            
            for node in current_level:
                level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            result.append(sum(level_nodes)/len(level_nodes))
            current_level = next_level
        return result

"""
Runtime: 52 ms, faster than 67.55% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
"""