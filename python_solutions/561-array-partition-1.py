# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        count = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                count += nums[i]
                
        return count
        
"""
Runtime: 288 ms, faster than 76.43% of Python3 online submissions for Array Partition I.
Memory Usage: 15.1 MB, less than 6.06% of Python3 online submissions for Array Partition I.
"""
