# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rst = []
        while matrix:
            rst += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return rst
        
"""
Runtime: 32 ms, faster than 16.50% of Python3 online submissions for Spiral Matrix.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
"""
