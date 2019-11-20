# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        a = []
        for i in nums:
            for j in nums:
                for k in nums:
                    if i + j + k == 0:
                        a.append(i,j,k)
        return a
        
