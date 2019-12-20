# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # ref: https://juejin.im/post/5d2bbfeef265da1b9613343f
        check = set(A[0])
        
        temp = [[l] * min([a.count(l) for a in A]) for l in check]
        
        result = []
        for i in temp:
            result += i
        
        return result
        
"""
Runtime: 36 ms, faster than 99.16% of Python3 online submissions for Find Common Characters.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Common Characters.
"""
