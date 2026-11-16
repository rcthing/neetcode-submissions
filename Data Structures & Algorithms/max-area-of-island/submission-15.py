class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            if i + 1 < ROWS and grid[i+1][j]: area += dfs(i+1, j)
            if i > 0 and grid[i-1][j]: area += dfs(i-1, j)
            if j + 1 < COLS and grid[i][j+1]: area += dfs(i, j+1)
            if j > 0 and grid[i][j-1]: area += dfs(i, j-1)
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        return res