class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def helper(n):
            if (n in memo):
                return memo[n]
            res = float('inf')
            for coin in coins:
                if (n>=coin):
                    res = min(res, helper(n-coin)+1)
            memo[n] = res
            return res
        return helper(amount) if (helper(amount) != float('inf')) else -1