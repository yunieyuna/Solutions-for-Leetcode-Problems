# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [i for i in (A + ' ' + B).split() if (A + ' ' + B).split().count(i) == 1]
        
"""
Runtime: 32 ms, faster than 62.56% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
"""
