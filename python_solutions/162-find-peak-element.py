# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid+1
        return l

"""
Runtime: 48 ms, faster than 40.64% of Python3 online submissions for Find Peak Element.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
"""