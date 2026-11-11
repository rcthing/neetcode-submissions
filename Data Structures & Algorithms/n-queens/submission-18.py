class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set() #(r + c)
        negDiag = set() #(r - c)

        curConfig = [["."] * n for _ in range(n)]
        def dfs(row):
            if row == n:
                copy = ["".join(row) for row in curConfig]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or row-col in negDiag or row+col in posDiag:
                    continue
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                curConfig[row][col] = "Q"

                dfs(row + 1)

                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                curConfig[row][col] = "."

        dfs(0)
        return res

            