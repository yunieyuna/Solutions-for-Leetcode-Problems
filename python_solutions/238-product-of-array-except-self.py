# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # reference: https://blog.csdn.net/coder_orz/article/details/52071951
        res = [0] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res