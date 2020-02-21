# https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 9
        cur_sum = base
        pre_sum = 0
        
        for i in range(1, 100000):
            if n <= cur_sum:
                div, mod = divmod(n - pre_sum - 1, i)
                num = 10 ** (i-1) + div
                return int(str(num)[mod])
            
            base = (10 ** (i)) * (i + 1) * 9
            pre_sum = cur_sum
            cur_sum += base
            
"""
Runtime: 28 ms, faster than 63.28% of Python3 online submissions for Nth Digit.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Nth Digit.
"""
