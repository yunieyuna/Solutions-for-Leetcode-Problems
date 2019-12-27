# https://leetcode.com/problems/intersection-of-two-arrays/

from itertools import chain

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        rst = set1.intersection(set2)
        return list(rst)
        
"""
Runtime: 60 ms, faster than 28.26% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.
"""
