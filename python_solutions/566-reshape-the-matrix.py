# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        num=[]
        for n in nums:
            num.extend(n)
        lens=len(num)
        if r*c==lens:
            temp=[]
            nu=[]
            i=0
            for k in range(r):
                for j in range(c):
                    temp.append(num[i])
                    i+=1
                nu.append(temp)
                temp=[]
            return nu
        else:
            return nums

"""
Runtime: 100 ms, faster than 76.25% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reshape the Matrix.
"""