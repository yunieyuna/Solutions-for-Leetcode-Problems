# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]

"""
Runtime: 40 ms, faster than 51.52% of Python3 online submissions for Word Break.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Break.
"""