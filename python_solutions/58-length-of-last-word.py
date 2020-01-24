# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s.split(' ')) == 0:
            return 0
        else:       
            return len(s.split(' ')[-1])
            
"""
Runtime: 60 ms, faster than 6.86% of Python3 online submissions for Length of Last Word.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Length of Last Word.
"""
