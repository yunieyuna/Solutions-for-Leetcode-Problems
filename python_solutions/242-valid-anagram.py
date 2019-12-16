# https://leetcode.com/problems/valid-anagram/

# method 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(list(s))
        list_t = sorted(list(t))
        return True if list_s == list_t else False
        
"""
Runtime: 48 ms, faster than 77.12% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.2 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
"""

# method 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alpha = {}
        beta = {}
        for c in s:
            alpha[c] = alpha.get(c, 0) + 1 # dict.get(A, B) => search A in dict, if no, return B
        for c in t:
            beta[c] = beta.get(c, 0) + 1
        return alpha == beta
        
"""
Runtime: 48 ms, faster than 77.12% of Python3 online submissions for Valid Anagram.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
"""
