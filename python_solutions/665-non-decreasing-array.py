# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        one, two = nums.copy(), nums.copy()
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
        
"""
Runtime: 232 ms, faster than 19.24% of Python3 online submissions for Non-decreasing Array.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
"""
