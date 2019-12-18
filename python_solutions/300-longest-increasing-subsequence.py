# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        
        if size <= 1:
            return size
        
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        
"""
Runtime: 1184 ms, faster than 23.63% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.
"""
