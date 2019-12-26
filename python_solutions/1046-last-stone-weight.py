# https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
            
        return -h[0]
        
"""
Runtime: 24 ms, faster than 95.84% of Python3 online submissions for Last Stone Weight.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
"""
