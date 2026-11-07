class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def backtrack(i, j, index):
            if index == len(word):
                return True
            elif (i < 0 or i >= rows or j < 0 or j >= cols
                    or word[index] != board[i][j] or (i, j) in seen):
                return False

            seen.add((i, j))
            res = (backtrack(i+1, j, index + 1) or
                    backtrack(i-1, j, index + 1) or
                    backtrack(i, j+1, index + 1) or
                    backtrack(i, j-1, index + 1))

            seen.discard((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False
