# https://leetcode.com/problems/permutations/

# for method 1
from itertools import permutations

class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
        # # method 1: use package itertools
        # return list(permutations(nums))
    
    # method 2: Recursion 递归
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        
        ans = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                ans.append([nums[i]] + j)
        return ans
        
