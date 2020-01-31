# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # ref: https://leetcode-cn.com/problems/triangle/solution/dong-tai-gui-hua-jiu-di-xiu-gai-o1kong-jian-python/
        if(not triangle):
            return 0
        n=len(triangle)
        if(n==1):
            return triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if(j==0):
                    triangle[i][j]+=triangle[i-1][j]
                elif(j==len(triangle[i])-1):
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
        
"""
Runtime: 60 ms, faster than 63.25% of Python3 online submissions for Triangle.
Memory Usage: 13.7 MB, less than 33.33% of Python3 online submissions for Triangle.
"""
