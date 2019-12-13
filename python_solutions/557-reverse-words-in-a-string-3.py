# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ").join([i[::-1] for i in s.split(" ")])
        
"""
Runtime: 32 ms, faster than 89.04% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 13.2 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.
"""
