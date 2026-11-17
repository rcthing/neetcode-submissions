from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dr = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j,0))
                    visited.add((i,j))
        while q:
            i, j, dist = q.popleft()
            grid[i][j] = dist

            for l, r in dr:
                if i+l >= 0 and j+r >= 0 and i+l < ROWS and j+r < COLS and (i+l, j+r) not in visited and grid[i+l][j+r] != -1:
                    q.append((i+l, j+r, dist + 1))
                    visited.add((i+l, j+r))



