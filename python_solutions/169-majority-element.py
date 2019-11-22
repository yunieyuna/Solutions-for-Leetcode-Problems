# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 通过set()去重，然后再比较每个元素的出现次数
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) > (len(nums)/2) :
                return i