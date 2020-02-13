# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res =[]
        # 首先判断正负，异或作用就是两个数不同为True，即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
            
        numerator, denominator = abs(numerator), abs(denominator)
        
        # 判断是否有小数
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        
        # 无小数
        if b == 0:
            return "".join(res)
        
        res.append(".")
        
        # 处理余数
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
                
            loc[b] = len(res)
            
        return  "".join(res)
        
"""
Runtime: 16 ms, faster than 99.55% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Fraction to Recurring Decimal.
"""
