# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        rst = [0 for _ in range(len(A))]
        for i in range(len(A)):
            rst[i] = (A[i])**2
        return sorted(rst)
        
"""
Runtime: 240 ms, faster than 84.58% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 14.8 MB, less than 94.05% of Python3 online submissions for Squares of a Sorted Array.
"""
