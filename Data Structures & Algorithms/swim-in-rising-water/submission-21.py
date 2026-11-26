from heapq import heapify, heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        n = len(grid)
        visited = set()

        while heap:
            h, i, j = heappop(heap)
            if i == j == n-1:
                return h
            if (i,j) in visited:
                continue
            
            visited.add((i,j))

            for k,l in ((0,1),(1,0),(-1,0),(0,-1)):
                ni = i + k
                nj = j + l
                if 0 <= ni < n and 0 <= nj < n:
                    heappush(heap, (max(h, grid[ni][nj]),ni,nj))

            
            

        
