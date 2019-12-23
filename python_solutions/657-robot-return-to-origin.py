# https://leetcode.com/problems/robot-return-to-origin/

# method 1
import numpy as np

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # method 1
        movements = {
            "U": np.array([0,1]),
            "D": np.array([0,-1]),
            "L": np.array([-1,0]),
            "R": np.array([1,0])
        }

        position = np.array([0,0])

        for move in moves:
            position += movements[move]

        if (position == np.array([0,0])).all():
            return True
        else:
            return False
            
"""
Runtime: 340 ms, faster than 5.16% of Python3 online submissions for Robot Return to Origin.
Memory Usage: 32.1 MB, less than 6.90% of Python3 online submissions for Robot Return to Origin.
"""



# method 2
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # method 2
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
        
"""
Runtime: 60 ms, faster than 63.74% of Python3 online submissions for Robot Return to Origin.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Robot Return to Origin.
"""
