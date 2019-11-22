# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = nums.count(0)
        
        for i in range(count0):
            nums.remove(0)
        nums.extend([0]*count0)