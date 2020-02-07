# https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen =[0] * len(nums)
        res = 0
        
        for i in nums:
            count = 0
            j = i
            while not seen[j]:
                seen[j] = 1
                count += 1
                j = nums[j]
            res = max(res, count)
            
        return res
        
"""
Runtime: 128 ms, faster than 45.69% of Python3 online submissions for Array Nesting.
Memory Usage: 15.2 MB, less than 12.50% of Python3 online submissions for Array Nesting.
"""
