# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False

"""
Runtime: 44 ms, faster than 15.16% of Python3 online submissions for Power of Two.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Two.
"""
