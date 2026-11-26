from heapq import heapify, heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        heappush(heap, (grid[0][0], 0, 0))
        n = len(grid)
        visited = set()

        while heap:
            h, i, j = heappop(heap)
            if i == j == n-1:
                return h
            if (i,j) in visited:
                continue
            
            visited.add((i,j))

            if 0 <= i+1 < n:
                heappush(heap, (max(h, grid[i+1][j]), i+1, j))
            if 0 <= i-1 < n:
                heappush(heap, (max(h, grid[i-1][j]), i-1, j))
            if 0 <= j+1 < n:
                heappush(heap, (max(h, grid[i][j+1]), i, j+1))
            if 0 <= j-1 < n:
                heappush(heap, (max(h, grid[i][j-1]), i, j-1))

            
            

        
