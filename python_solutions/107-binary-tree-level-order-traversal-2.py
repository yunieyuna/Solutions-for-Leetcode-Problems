# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        cur = [root]
        
        while cur:
            cur_layer_val = []
            next_layer_node = []
            for node in cur:
                if node:
                    cur_layer_val.append(node.val)
                    next_layer_node.extend([node.left, node.right])
            if cur_layer_val:
                queue.insert(0, cur_layer_val)
            cur = next_layer_node
        return queue
        
"""
Runtime: 28 ms, faster than 91.56% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
