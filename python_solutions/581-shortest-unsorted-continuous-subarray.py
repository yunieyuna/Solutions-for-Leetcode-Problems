# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 源地址：https://blog.csdn.net/fuxuemingzhu/article/details/79254454
        # 因为题目中的数组的长度最大只有1000，所以排序的时间不算很高。排序后的数组和之前的数组进行比较，找出最小的不相等的数字位置和最大不相等的数字的位置，两者的差相减+1即为所求。
        
        # method 1
        length, sorted_nums = len(nums), sorted(nums)
        
        if nums == sorted_nums:
            return 0
        
        l = min([i for i in range(length) if nums[i] != sorted_nums[i]])
        r = max([i for i in range(length) if nums[i] != sorted_nums[i]])
        
        return r - l + 1
