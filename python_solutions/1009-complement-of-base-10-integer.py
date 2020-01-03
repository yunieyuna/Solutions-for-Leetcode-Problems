# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        a = bin(N)[2:]
        b = ""
        for i in range(len(a)):
            x = int(a[i]) ^ 1
            b = b + str(x)
        return int(b, 2)

"""
Runtime: 24 ms, faster than 88.92% of Python3 online submissions for Complement of Base 10 Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Complement of Base 10 Integer.
"""