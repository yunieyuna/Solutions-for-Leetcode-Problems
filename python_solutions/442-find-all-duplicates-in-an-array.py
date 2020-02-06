# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] *= -1
            else:
                res.append(abs(n))

        return res

"""
Runtime: 404 ms, faster than 45.19% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 20.2 MB, less than 35.71% of Python3 online submissions for Find All Duplicates in an Array.
"""
