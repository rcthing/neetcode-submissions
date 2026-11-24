from collections import defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return -1

        adj = defaultdict(list)
        for t in times:
            adj[t[0]].append((t[1],t[2]))

        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            time, node = heappop(minHeap)
            if node in visited:
                continue

            visited.add(node)
            if len(visited) == n:
                return time
                break

            for nei in adj[node]:
                if nei[0] not in visited:
                    heappush(minHeap, (time + nei[1], nei[0]))
        return -1





        
        