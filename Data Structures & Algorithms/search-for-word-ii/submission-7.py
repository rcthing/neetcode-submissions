class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.index = -1

    def addWord(self, word, i):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.endOfWord = True
        cur.index = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i,word in enumerate(words):
            root.addWord(word, i)

        height, lenght = len(board) - 1, len(board[0]) - 1
        ans = []
        path = set()

        def dfs(i, j, root):
            if (i < 0 or j < 0 or i > height or
             j > lenght or (i, j) in path or
              board[i][j] not in root.children):
                return

            cur = root.children[board[i][j]]
            path.add((i, j))

            if cur.endOfWord and cur.index != -1:
                ans.append(words[cur.index])
                cur.index = -1

            dfs(i+1, j, cur)
            dfs(i-1, j, cur)
            dfs(i, j+1, cur)
            dfs(i, j-1, cur)

            path.remove((i, j))
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

    
        return ans