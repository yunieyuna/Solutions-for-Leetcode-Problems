# https://leetcode.com/problems/bulls-and-cows/

from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)
        
"""
Runtime: 36 ms, faster than 81.40% of Python3 online submissions for Bulls and Cows.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.
"""
