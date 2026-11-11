class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set() #(r + c)
        negDiag = set() #(r - c)

        curConfig = [["."] * n for i in range(n)]
        def dfs(row):
            if row >= n:
                copy = ["".join(row) for row in curConfig]
                res.append(copy)
                return

            for col in range(n):
                if (col not in cols and row-col not in negDiag 
                    and row+col not in posDiag):
                    cols.add(col)
                    posDiag.add(row+col)
                    negDiag.add(row-col)
                    curConfig[row][col] = "Q"
                    dfs(row + 1)

                    cols.discard(col)
                    posDiag.discard(row+col)
                    negDiag.discard(row-col)
                    curConfig[row][col] = "."

        dfs(0)
        return res

            