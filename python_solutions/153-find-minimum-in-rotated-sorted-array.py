# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search_min(left, right):
            if nums[right] >= nums[left]:
                return nums[left]
            else:
                mid = (left + right) >> 1
                return min(search_min(left, mid), search_min(mid+1, right))
            
        return search_min(0, len(nums)-1)
        
"""
Runtime: 48 ms, faster than 15.13% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
"""
