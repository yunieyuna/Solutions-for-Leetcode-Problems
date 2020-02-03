# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp+[s[:i]])
        helper(s, [])
        return res
        
"""
Runtime: 84 ms, faster than 62.05% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Palindrome Partitioning.
"""
