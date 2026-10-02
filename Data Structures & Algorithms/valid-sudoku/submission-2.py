class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hset = set()

        for i in range(len(board)):
            hset.clear()
            for j in range(len(board[0])):
                if board[i][j] in hset:
                    return False
                if board[i][j] != ".":
                    hset.add(board[i][j])

        for j in range(len(board[0])):
            hset.clear()
            for i in range(len(board)):
                if board[i][j] in hset:
                    return False
                if board[i][j] != ".":
                    hset.add(board[i][j])

        for k in range(3):
            for l in range(3):
                hset.clear()
                for i in range(k * 3, k * 3 + 3):
                    for j in range(l * 3, l * 3 + 3):
                        if board[i][j] in hset:
                            return False
                        if board[i][j] != ".":
                            hset.add(board[i][j])

        return True

