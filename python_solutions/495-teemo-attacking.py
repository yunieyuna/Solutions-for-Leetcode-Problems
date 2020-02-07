# https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or not duration:
            return 0
        
        if duration == 0:
            return 0
        
        total = 0
        for i in range(0, len(timeSeries)-1):
            if timeSeries[i] + duration >= timeSeries[i+1]:
                total += timeSeries[i+1] - timeSeries[i]
            else:
                total += duration
        total += duration
        
        return total
        
"""
Runtime: 284 ms, faster than 55.02% of Python3 online submissions for Teemo Attacking.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Teemo Attacking.
"""
