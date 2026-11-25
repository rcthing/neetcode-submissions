from heapq import heapify, heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        minHeap = []
        n = len(points)
        visited = set()
        res = 0
        heappush(minHeap, (0,0))

        while len(visited) < n:
            dist, i = heappop(minHeap)
            if i in visited:
                continue
            
            visited.add(i)
            res += dist

            for j in range(n):
                if j not in visited:
                    heappush(minHeap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))

        return res



