class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, posDiag, negDiag = set(), set(), set()

        curConfig = []
        def dfs(row):
            if row >= n:
                res.append(curConfig.copy())
                return

            for col in range(n):
                if (col not in cols and row-col not in negDiag 
                    and row+col not in posDiag):
                    cols.add(col)
                    posDiag.add(row+col)
                    negDiag.add(row-col)
                    curConfig.append("." * col + "Q" + "." * (n-col - 1))
                    dfs(row + 1)
                    
                    cols.discard(col)
                    posDiag.discard(row+col)
                    negDiag.discard(row-col)
                    curConfig.pop()

        dfs(0)
        return res

            