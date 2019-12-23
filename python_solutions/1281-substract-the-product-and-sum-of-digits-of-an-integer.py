# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        for i in str(n):
            product = product * int(i)
            
        sum_v = sum([int(i) for i in str(n)])
        return product - sum_v
        
"""
Runtime: 28 ms, faster than 56.98% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""
