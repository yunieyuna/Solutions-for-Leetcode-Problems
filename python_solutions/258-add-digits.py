# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        sum_num = sum(map(int, list(str(num))))
        
        while sum_num >= 10:
            sum_num = sum(map(int, list(str(sum_num))))
            
        return sum_num
        
"""
Runtime: 32 ms, faster than 50.56% of Python3 online submissions for Add Digits.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Digits.
"""
