# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x*x
            
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False
        
"""
Runtime: 28 ms, faster than 68.27% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Perfect Square.
"""
