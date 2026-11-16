class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        res = []
        ROWS, COLS = len(board), len(board[0])
        def addWord(root, word, index):
            for c in word:
                if c not in root.children:
                    root.children[c] = TrieNode()
                root = root.children[c]
            root.index = index

        root = TrieNode()
        for i, word in enumerate(words):
            addWord(root, word, i)

        def dfsSearch(i, j, root):
            if root.index > -1:
                res.append(words[root.index])
                root.index = -1
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] not in root.children:
                return

            root = root.children[board[i][j]]
            copy = board[i][j]
            board[i][j] = "#"
            
            dfsSearch(i+1, j, root)
            dfsSearch(i-1, j, root)
            dfsSearch(i, j+1, root)
            dfsSearch(i, j-1, root)
            board[i][j] = copy

        for i in range(ROWS):
            for j in range(COLS):
                dfsSearch(i, j, root)
        return res
            

        