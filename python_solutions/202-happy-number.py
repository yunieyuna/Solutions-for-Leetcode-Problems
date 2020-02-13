# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {1}
    
        while n not in seen:
            seen.add(n)
            
            n = sum(int(i)**2 for i in str(n))
            
        return n == 1
        
"""
Runtime: 36 ms, faster than 34.41% of Python3 online submissions for Happy Number.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Happy Number.
"""
