# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            n, y = divmod(n, 26) 
            res = chr(y + 65) + res
        return res
        
"""
Runtime: 24 ms, faster than 85.09% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
"""
