from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dr = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            i, j = q.popleft()

            for l, r in dr:
                if i+l >= 0 and j+r >= 0 and i+l < ROWS and j+r < COLS and grid[i+l][j+r] == INF:
                    grid[i+l][j+r] = grid[i][j] + 1
                    q.append((i+l, j+r))
                    visited.add((i+l, j+r))



