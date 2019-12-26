# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R = len(A)
        C = len(A[0])

        rst = [[0 for _ in range(R)] for _ in range(C)]

        for r in range(R):
            for c in range(C):
                rst[c][r] = A[r][c]

        return rst
        
"""
Runtime: 80 ms, faster than 63.50% of Python3 online submissions for Transpose Matrix.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Transpose Matrix.
"""
