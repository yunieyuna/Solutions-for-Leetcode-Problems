# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        res, muls = 10, 9
        
        for i in range(1, min(n, 10)):
            muls *= 10 - i
            res += muls
        
        return res
        
***
Runtime: 28 ms, faster than 61.92% of Python3 online submissions for Count Numbers with Unique Digits.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Count Numbers with Unique Digits.
***
