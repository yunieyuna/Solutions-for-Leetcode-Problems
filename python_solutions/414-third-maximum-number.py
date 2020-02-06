# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = sorted(list(set(nums)))
        if len(temp) >= 3:
            return temp[-3]
        else:
            return temp[-1]
            
"""
Runtime: 52 ms, faster than 72.92% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.2 MB, less than 30.77% of Python3 online submissions for Third Maximum Number.
"""
