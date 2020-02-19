# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, num: int) -> bool:
        while True:
            last = num
            if not num % 2:  ## 如果2整除num，就除以2
                num >>= 1
            if not num % 3:  ## 如果3整除num，就除以3
                num //= 3
            if not num % 5:  ## 如果5整除num，就除以5
                num //= 5
            if num == 1:  ## 如果若干次操作后，num变成1，说明num的因数只有2、3、5，是丑数
                return True
            if last == num:  ## 如果1轮操作后，num没变，说明num不是丑数
                return False
                
"""
Runtime: 28 ms, faster than 76.42% of Python3 online submissions for Ugly Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Ugly Number.
"""
