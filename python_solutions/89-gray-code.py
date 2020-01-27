# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:
            return [0]

        res=[]

        def back(now,x):
            if len(now)==n:
                res.append(int(now,2))
            elif x==0:
                back(now+'0',0)
                back(now+'1',1)
            else:
                back(now+'1',0)
                back(now+'0',1)
        
        back('',0)
        return res
        
"""
Runtime: 36 ms, faster than 25.60% of Python3 online submissions for Gray Code.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Gray Code.
"""
