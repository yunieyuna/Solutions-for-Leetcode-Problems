# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        set_J = set(J)
        count = 0
        for s in S:
            if s in set_J:
                count += 1
        return count
        
"""
Runtime: 28 ms, faster than 87.58% of Python3 online submissions for Jewels and Stones.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
"""
