# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                starting_station = i+1
                curr_tank = 0
        return starting_station if total_tank >= 0 else -1
        
"""
Runtime: 48 ms, faster than 90.85% of Python3 online submissions for Gas Station.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Gas Station.
"""
