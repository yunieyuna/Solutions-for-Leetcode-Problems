# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        rest = 0
        hold = -float("inf")
        
        for p in prices:
            pre_sold = sold
            sold = hold + p
            hold = max(hold, rest - p)
            rest = max(rest, pre_sold)
        
        return max(rest, sold)
        
"""
Runtime: 36 ms, faster than 93.14% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
"""
