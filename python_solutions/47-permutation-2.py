# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        # 修改1： 首先排序，之后才有可能发现重复分支，升序/倒叙均可
        nums.sort()
        # nums.sort(reversed = True)
        
        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res
    
    def __dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                # 修改 2：因为排序以后重复的数一定不会出现在开始，故 i > 0
                # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
                # 这种情况跳过即可
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                self.__dfs(nums, index + 1, pre, used, res)
                used[i] = False
                pre.pop()
                
"""
Runtime: 56 ms, faster than 84.57% of Python3 online submissions for Permutations II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations II.
"""
