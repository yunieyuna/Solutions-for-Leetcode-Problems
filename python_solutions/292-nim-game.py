# https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n % 4 != 0)
        
"""
Runtime: 28 ms, faster than 69.84% of Python3 online submissions for Nim Game.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Nim Game.
"""
