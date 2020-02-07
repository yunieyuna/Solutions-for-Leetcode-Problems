# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        
"""
Runtime: 280 ms, faster than 60.38% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Product of Three Numbers.
"""
