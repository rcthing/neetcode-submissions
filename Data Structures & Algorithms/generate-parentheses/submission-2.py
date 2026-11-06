class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(i, op, cl, subset):
            if i == 2 * n or cl > op:
                if op == cl:
                    res.append(subset)
                return

            subset += "("
            backtrack(i + 1, op + 1, cl, subset)

            subset = subset[:-1]
            subset += ")"
            backtrack(i + 1, op, cl + 1, subset)

        backtrack(0, 0, 0, "")
        return res



            