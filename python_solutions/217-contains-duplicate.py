# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        if (len(nums) - len(set(nums))) == 0:
            return False
        return True
