# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_sum = nums1 + nums2
        num_sum.sort()
        if len(num_sum) % 2 == 0:
            return float((num_sum[int(len(num_sum)/2-1)] + num_sum[int(len(num_sum)/2)])/2)
        else:
            return float(num_sum[int((len(num_sum)-1)/2)])
            
