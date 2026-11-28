class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        fcost = [0] * n
        fcost[0], fcost[1] = cost[0], cost[1]

        for i in range(2, n):
            fcost[i] = cost[i] + min(fcost[i-1], fcost[i-2])
        
        return min(fcost[n-1], fcost[n-2])


