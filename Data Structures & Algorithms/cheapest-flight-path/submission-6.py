class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for f, t, c in flights:
            adj[f].append((t,c))
        
        cost = [float("inf")] * n
        cost[src] = 0
        nxt = cost.copy()

        for _ in range(k + 1):
            for node in adj:
                for nei, c in adj[node]:
                    if cost[node] + c < nxt[nei]:
                        nxt[nei] = cost[node] + c
            cost = nxt.copy()

        if cost[dst] != float("inf"):
            return cost[dst]
        return -1
