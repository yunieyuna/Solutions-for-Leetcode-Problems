# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

"""
Runtime: 144 ms, faster than 29.46% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 13.3 MB, less than 97.44% of Python3 online submissions for Set Matrix Zeroes.
"""
