class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Q Cost is always positive ?
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        min_cost = [1000] * (n+1)
        min_cost[0] = 0
        min_cost[1] = 0

        for i in range(2, n+1, 1):
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])
            # print(min_cost[i])
            # print(min_cost[i-1],cost[i-1])
            # print(min_cost[i-2],cost[i-2])

        return min_cost[n]
