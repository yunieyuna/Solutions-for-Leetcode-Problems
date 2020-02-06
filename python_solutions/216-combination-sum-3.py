# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def helper(count,i,tmp,target):
            # print(count,i,tmp,target)
            if count==k:
                if target==0:
                    res.append(tmp)
                return
            for j in range(i,10):
                if j>target:
                    break
                helper(count+1,j+1,tmp+[j],target-j)
        helper(0,1,[],n)
        return res

"""
Runtime: 24 ms, faster than 95.07% of Python3 online submissions for Combination Sum III.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Combination Sum III.
"""
