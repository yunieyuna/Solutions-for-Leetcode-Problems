# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        a = 1
        b = 1
        for i in range(N-1):
            a, b = b, a+b
        return a
