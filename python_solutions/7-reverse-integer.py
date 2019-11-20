# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        reversed_int = int(str(abs(x))[::-1])
        if reversed_int >= 2 ** 31 - 1 or x == 0:
            return 0
        
        return reversed_int * -1 if x < 0 else reversed_int
