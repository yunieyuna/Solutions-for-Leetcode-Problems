# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        
        # 把除数不断的左移，直到它大于被除数
        # Move dividend to left until it's bigger than divisor
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count # 这里的位移运算把二进制转换为十进制
                dividend -= divisor
        if sign: result = -result
            
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1
        
"""
Runtime: 24 ms, faster than 94.72% of Python3 online submissions for Divide Two Integers.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Divide Two Integers.
"""
