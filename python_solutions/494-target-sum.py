# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # ref: https://blog.csdn.net/Dby_freedom/article/details/84973941
        
        length = len(nums)
        dp = [collections.defaultdict(int) for _ in range(length + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for key,value in dp[i].items():
                dp[i+1][key+num] += value
                dp[i+1][key-num] += value
                
        return dp[length][S]
        
"""
Runtime: 200 ms, faster than 83.55% of Python3 online submissions for Target Sum.
Memory Usage: 13.1 MB, less than 91.67% of Python3 online submissions for Target Sum.
"""
