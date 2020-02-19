# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** round(math.log(n, 3)) == n
        
"""
Runtime: 92 ms, faster than 24.51% of Python3 online submissions for Power of Three.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Three.
"""
