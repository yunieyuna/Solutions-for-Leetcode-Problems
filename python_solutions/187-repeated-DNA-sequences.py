# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s) - 9):
            if s[i: i+10] in d:
                d[s[i: i+10]] = True
            else:
                d[s[i: i+10]] = False
                
        return filter(lambda i: d[i], d)
        
"""
Runtime: 80 ms, faster than 26.67% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 27.1 MB, less than 16.67% of Python3 online submissions for Repeated DNA Sequences.
"""
