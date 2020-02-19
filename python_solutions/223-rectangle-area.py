# https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        res = 0
        
        # area 1
        res += (C - A)*(D - B)
        
        # area 2
        res += (G - E)*(H - F)
        
        # intersected area
        width = min(C, G) - max(A, E)
        height = min(D, H) - max(B, F)
        
        if width > 0 and height > 0:
            res -= width * height
        
        return res
        
"""
Runtime: 52 ms, faster than 55.80% of Python3 online submissions for Rectangle Area.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rectangle Area.
"""
