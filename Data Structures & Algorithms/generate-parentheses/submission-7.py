class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(i, op, cl, subset):
            if op == cl == n:
                res.append(subset)
                return

            if op < n:
                subset += "("
                backtrack(i + 1, op + 1, cl, subset)
                subset = subset[:-1]
            if cl < op:
                subset += ")"
                backtrack(i + 1, op, cl + 1, subset)


        backtrack(0, 0, 0, "")
        return res



            