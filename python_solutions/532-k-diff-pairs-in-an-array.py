# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        if k<0:
            return 0

        s, r = set(), set()
        for n in nums:
            if n + k in s:
                r.add(n + k)
            if n - k in s:
                r.add(n)
            s.add(n)

        return len(r)

"""
Runtime: 120 ms, faster than 97.13% of Python3 online submissions for K-diff Pairs in an Array.
Memory Usage: 14.8 MB, less than 70.97% of Python3 online submissions for K-diff Pairs in an Array.
"""
