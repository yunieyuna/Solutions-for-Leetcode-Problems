# https://leetcode.com/problems/water-and-jug-problem/

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or (z - x <= y and z % self.gcd(x, y) == 0)
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
        
"""
Runtime: 24 ms, faster than 83.48% of Python3 online submissions for Water and Jug Problem.
Memory Usage: 12.4 MB, less than 100.00% of Python3 online submissions for Water and Jug Problem.
"""
