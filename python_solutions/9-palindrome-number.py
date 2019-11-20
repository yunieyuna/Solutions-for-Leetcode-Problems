# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        思路：1. 负数的话一定不是
             2. 用[::-1]来做reverse
        """
        
        if x < 0:
            return False
        else:
            reversed_int = int(str(x)[::-1])
            return x == reversed_int
