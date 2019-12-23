# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[j ^ 1 for j in row[::-1]] for row in A]
        
"""
Runtime: 48 ms, faster than 91.07% of Python3 online submissions for Flipping an Image.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Flipping an Image.
"""
