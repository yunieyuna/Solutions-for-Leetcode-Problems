# https://leetcode.com/problems/perfect-squares/submissions/

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt
        
"""
Runtime: 184 ms, faster than 81.05% of Python3 online submissions for Perfect Squares.
Memory Usage: 13.6 MB, less than 70.00% of Python3 online submissions for Perfect Squares.
"""
