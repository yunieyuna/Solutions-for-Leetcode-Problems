# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         # method 1: Traversal 2 times
#         N = len(A)
#         ans = [None] * N
        
#         t = 0
#         for i, x in enumerate(A):
#             if x % 2 == 0:
#                 ans[t] = x
#                 t += 2
        
#         t = 1
#         for i, x in enumerate(A):
#             if x % 2 == 1:
#                 ans[t] = x
#                 t += 2
        
#         return ans
    
        # method 2: Dual-pointers
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
        
"""
Runtime: 220 ms, faster than 94.76% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Sort Array By Parity II.
"""
