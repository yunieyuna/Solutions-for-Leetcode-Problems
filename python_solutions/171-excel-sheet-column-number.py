# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        bit = 1
        
        for a in s[::-1]:
            res += (ord(a) - 64) * bit
            bit *= 26
        return res
        
"""
Runtime: 28 ms, faster than 81.01% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
"""
