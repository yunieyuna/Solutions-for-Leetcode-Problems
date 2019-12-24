# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low = 0
        high = len(S)
        
        rst = []
        
        for s in S:
            if s == "I":
                rst.append(low)
                low += 1
                
            if s == "D":
                rst.append(high)
                high -= 1
                
        return rst + [low]
        
"""
Runtime: 64 ms, faster than 89.52% of Python3 online submissions for DI String Match.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for DI String Match.
"""
