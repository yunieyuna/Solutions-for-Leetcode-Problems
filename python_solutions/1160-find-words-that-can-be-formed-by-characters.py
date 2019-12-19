# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        return ans
        
"""
Runtime: 236 ms, faster than 36.70% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
"""
