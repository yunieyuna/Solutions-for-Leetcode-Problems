# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return min(max(-2**31, x**n), 2**31 - 1)
        
"""
Runtime: 24 ms, faster than 87.98% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
"""
