# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        a, b = n // 3, n % 3
        if b == 0:
            return pow(3, a)
        if b == 1:
            return pow(3, a - 1) * 4
        if b == 2:
            return pow(3, a) * b
            
"""
Runtime: 20 ms, faster than 98.51% of Python3 online submissions for Integer Break.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer Break.
"""
