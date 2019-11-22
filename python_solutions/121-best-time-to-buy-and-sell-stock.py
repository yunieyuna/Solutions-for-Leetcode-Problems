# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        try:
            minprice = prices[0]
        except:
            prices = [0]
        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            maxprofit = max(maxprofit, prices[i] - minprice)
        return maxprofit