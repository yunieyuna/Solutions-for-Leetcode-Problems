# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        
        s = sum(nums)
        if s & 1 == 1:
            return False
        
        target = s // 2
        dp = [[False for _ in range(target + 1)] for _ in range(size)]
        
        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True
        
        # i 表示物品索引
        for i in range(1, size):
            # j 表示背包容量
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[-1][-1]
        
"""
Runtime: 1940 ms, faster than 15.98% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 16.8 MB, less than 9.09% of Python3 online submissions for Partition Equal Subset Sum.
"""
