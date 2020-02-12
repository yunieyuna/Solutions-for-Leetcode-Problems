# https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n+1))
        for i in range(1, k):
            res[i:] = res[:i-1:-1]
        return res
        
"""
Runtime: 980 ms, faster than 6.20% of Python3 online submissions for Beautiful Arrangement II.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Beautiful Arrangement II.
"""
