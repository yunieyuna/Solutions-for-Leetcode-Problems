# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### Method 1
        # Time complexity: O(n^2)
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            if num == 1:
                count1 += 1
            if num == 2:
                count2 += 1
        for i in range(count0):
            nums[i] = 0
        for j in range(count1):
            nums[count0 + j] = 1
        for k in range(count2):
            nums[count0 + count1 + k] = 2