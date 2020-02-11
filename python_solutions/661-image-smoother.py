# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]
        
        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count
        
        return ans
        
"""
Runtime: 736 ms, faster than 64.04% of Python3 online submissions for Image Smoother.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Image Smoother.
"""
