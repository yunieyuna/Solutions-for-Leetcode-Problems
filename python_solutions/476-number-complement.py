# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
        
"""
Runtime: 40 ms, faster than 21.91% of Python3 online submissions for Number Complement.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number Complement.
"""
