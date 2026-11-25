from heapq import heapify, heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float("inf")] * n
        dist[0] = 0
        node, res = 0, 0
        connected = {0}

        while len(connected) < n:
            minD = float("inf")

            for i in range(n):
                if i not in connected:
                    d = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    dist[i] = min(dist[i], d)
                    if dist[i] < minD:
                        minD = dist[i]
                        nxt = i
            res += minD
            node = nxt
            connected.add(nxt)
        return res



            





