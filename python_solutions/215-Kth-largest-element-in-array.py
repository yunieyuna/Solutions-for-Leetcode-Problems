# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq # for method 2

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # method 1
        # return sorted(nums)[-k]
    
        # method 2
        return heapq.nlargest(k, nums)[-1]
        
"""
Runtime: 64 ms, faster than 93.31% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Kth Largest Element in an Array.
"""
