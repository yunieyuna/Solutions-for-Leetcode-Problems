# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = [[]]
        for i, v in dic.items():
            temp = res.copy()
            for j in res:
                temp.extend(j + [i]*(k + 1) for k in range(v))
            res = temp
        return res
        
"""
Runtime: 44 ms, faster than 24.50% of Python3 online submissions for Subsets II.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Subsets II.
"""
