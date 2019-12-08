# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for row in matrix:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 -i], row[i]
                
        return matrix

"""
Runtime: 36 ms, faster than 79.56% of Python3 online submissions for Rotate Image.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Rotate Image.
"""