# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        ma = max(P[i+k] - P[i] for i in range(len(nums) - k + 1))
        return ma / float(k)

"""
Runtime: 936 ms, faster than 49.05% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 16.3 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.
"""
