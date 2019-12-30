# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res

"""
Runtime: 48 ms, faster than 96.04% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Letter Case Permutation.
"""