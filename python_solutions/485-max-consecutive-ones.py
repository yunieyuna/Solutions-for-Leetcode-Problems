# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        max_count = 0
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            if nums[i] == 0:
                max_count = max(max_count, curr_count)
                curr_count = 0
                
        max_count = max(max_count, curr_count)
        
        return max_count
        
"""
Runtime: 396 ms, faster than 43.41% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones.
"""
