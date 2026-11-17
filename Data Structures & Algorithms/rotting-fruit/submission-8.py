from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        d = [(1,0), (0,1), (-1,0), (0,-1)]
        fresh, time = 0, 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh:
            for _ in range(len(q)):
                i, j = q.popleft()

                for l, r in d:
                    if i+l < 0 or j+r < 0 or i+l >= ROWS or j+r >= COLS or grid[i+l][j+r] != 1:
                        continue
                    grid[i+l][j+r] = 2
                    fresh -=1
                    q.append((i+l, j+r))
            time += 1
        
        return time if fresh == 0 else -1

