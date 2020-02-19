# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        
        while n >= 5:
            res += n // 5
            n //= 5
            
        return res
        
"""
Runtime: 24 ms, faster than 89.25% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Factorial Trailing Zeroes.
"""
