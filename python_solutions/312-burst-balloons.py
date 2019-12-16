# https://leetcode.com/problems/burst-balloons/

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]     # 初始化dp
        
        for k in range(2, n):                # k 确定一个滑动窗口的大小，从2开始
            for left in range(0, n - k):     # 滑动窗口，从左向右滑动，确定区间的开始（left）、结束（right）位置
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                    
        return dp[0][n - 1]
        
"""
Runtime: 452 ms, faster than 66.20% of Python3 online submissions for Burst Balloons.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Burst Balloons.
"""
