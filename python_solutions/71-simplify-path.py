# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
        return '/'+'/'.join(r)
        
"""
时间复杂度：O(n) (n为path中元素个数)
空间复杂度：O(n) (n为path中元素个数)
"""
