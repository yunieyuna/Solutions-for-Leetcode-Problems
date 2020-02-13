# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        for idx, citation in enumerate(citations):
            if idx >= citation:
                return idx
        
        return len(citations)
        
"""
Runtime: 36 ms, faster than 64.67% of Python3 online submissions for H-Index.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for H-Index.
"""
