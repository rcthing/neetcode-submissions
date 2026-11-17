from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        d = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q:
            i, j = q.popleft()

            for l, r in d:
                if i+l < 0 or j+r < 0 or i+l >= ROWS or j+r >= COLS or grid[i+l][j+r] != 1:
                    continue
                grid[i+l][j+r] = grid[i][j] + 1
                q.append((i+l, j+r))
        for row in grid:
            if 1 in row: 
                return -1
        
        return max(0, max(max(row) for row in grid) - 2)

