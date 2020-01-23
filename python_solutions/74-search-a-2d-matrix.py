# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        left, right = 0, m*n-1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False
        
"""
Runtime: 64 ms, faster than 78.24% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
"""
