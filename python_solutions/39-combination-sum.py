# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ref: https://www.twblogs.net/a/5c8371eabd9eee35cd69b6dd/zh-cn
        
        self.res = []
        if len(candidates) <= 0:
            return res
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.res
    
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.res.append(sublist)
        if target < candidates[0]:
            return
        for num in candidates:
            if num > target:
                return
            if num < last:
                continue
            self.dfs(candidates, sublist + [num], target - num, num)

"""
Runtime: 40 ms, faster than 99.86% of Python3 online submissions for Combination Sum.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Combination Sum.
"""