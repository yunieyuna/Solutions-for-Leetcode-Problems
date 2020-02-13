# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        return [*map(pattern.index, pattern)] == [*map(str.split(' ').index, str.split(' '))]
        
"""
Runtime: 20 ms, faster than 96.79% of Python3 online submissions for Word Pattern.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Word Pattern.
"""
