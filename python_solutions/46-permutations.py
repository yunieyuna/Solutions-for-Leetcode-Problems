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
        
# method 3: Recursion
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def backtrack(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
#         backtrack(nums, [])
#         return res

"""
Runtime: 32 ms, faster than 98.23% of Python3 online submissions for Permutations.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutations.
"""
