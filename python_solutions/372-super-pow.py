# https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337
        
        
    def qpow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x *x % m
            n >>= 1
        return ans
        
"""
Runtime: 148 ms, faster than 38.81% of Python3 online submissions for Super Pow.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Super Pow.
"""
