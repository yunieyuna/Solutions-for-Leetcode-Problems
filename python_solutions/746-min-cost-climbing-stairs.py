class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_0, min_cost_1 = 0, min(cost[0], cost[1])
        for i in range(2, len(cost)):
            min_cost = min(min_cost_1 + cost[i], min_cost_0 + cost[i - 1])
            min_cost_0, min_cost_1 = min_cost_1, min_cost
        return min_cost