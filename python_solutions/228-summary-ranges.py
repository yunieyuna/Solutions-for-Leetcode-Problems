# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        if(n==1):
            return [str(nums[0])]
        res=[]
        l=0
        r=0
        cur=0
        while(cur<n):
            while(cur<n and nums[cur]-nums[r]<=1):
                r=cur
                cur+=1
            if(l==r):
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l])+"->"+str(nums[r]))
            l=cur
            r=cur
        return res
        
"""
Runtime: 24 ms, faster than 86.36% of Python3 online submissions for Summary Ranges.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Summary Ranges.
"""
