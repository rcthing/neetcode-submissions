from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j,0))
                    visited.add((i,j))
        while q:
            i, j, dist = q.popleft()
            grid[i][j] = dist

            if i+1 >= 0 and j >= 0 and i+1 < ROWS and j < COLS and (i+1, j) not in visited and grid[i+1][j] != -1:
                q.append((i+1, j, dist + 1))
                visited.add((i+1,j))
            if i >= 0 and j+1 >= 0 and i < ROWS and j+1 < COLS and (i, j+1) not in visited and grid[i][j+1] != -1:
                q.append((i, j+1, dist + 1))
                visited.add((i,j+1))
            if i-1 >= 0 and j >= 0 and i-1 < ROWS and j < COLS and (i-1, j) not in visited and grid[i-1][j] != -1:
                q.append((i-1, j, dist + 1))
                visited.add((i-1,j))
            if i >= 0 and j-1 >= 0 and i < ROWS and j-1 < COLS and (i, j-1) not in visited and grid[i][j-1] != -1:
                q.append((i, j-1, dist + 1))
                visited.add((i,j-1))



