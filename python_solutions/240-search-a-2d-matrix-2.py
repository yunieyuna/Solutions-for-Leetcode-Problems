# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # corner cases
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        row = 0
        col = cols - 1
        
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False
                
"""
Runtime: 28 ms, faster than 97.48% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 17.3 MB, less than 96.30% of Python3 online submissions for Search a 2D Matrix II.
"""
