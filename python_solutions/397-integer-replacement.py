# https://leetcode.com/problems/integer-replacement/

class Solution:
    def integerReplacement(self, n, count = 0) -> int:
        if n == 1:
            return count
        if not n%2:
            return self.integerReplacement( n/2, count + 1)
        else:
            return min(self.integerReplacement( n+1, count + 1), self.integerReplacement( n-1, count + 1))
            
"""
Runtime: 300 ms, faster than 15.35% of Python3 online submissions for Integer Replacement.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer Replacement.
"""
