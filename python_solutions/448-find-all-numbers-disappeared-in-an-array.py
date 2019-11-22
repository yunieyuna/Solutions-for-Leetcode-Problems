# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums):
        length = len(nums) # 求数组长度
        nums.sort() # 排序数组
        num_set = set(nums) # 去重
        list_allset = set(list(range(1,length+1))) #定义一个从1到n开始的set
        return list(list_allset - num_set) #两个set相减便得到最终