# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
        
"""
Runtime: 92 ms, faster than 67.26% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Toeplitz Matrix.
"""
