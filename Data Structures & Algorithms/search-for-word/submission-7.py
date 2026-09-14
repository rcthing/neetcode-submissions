class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(i, j, cur_index):
            if cur_index == len(word):
                return True

            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0])-1 or board[i][j] != word[cur_index] or (i, j) in path:
                return False

            path.add((i, j))

            res = dfs(i+1, j, cur_index+1) or dfs(i-1, j, cur_index+1) or dfs(i, j+1, cur_index+1) or dfs(i, j-1, cur_index+1)

            path.remove((i,j))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False