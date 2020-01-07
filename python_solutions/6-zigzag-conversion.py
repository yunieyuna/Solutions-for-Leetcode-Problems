# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag  = -flag
            i += flag
        return "".join(res) 
        
"""
Runtime: 52 ms, faster than 86.24% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
"""
