class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(root, word, index):
            cur = root

            for i in range(index, len(word)):
                if word[i] == ".":
                    for ch in cur.children:
                        if dfs(cur.children[ch], word, i+1):
                            return True
                    return False

                if word[i] not in cur.children:
                    return False

                else:
                    cur = cur.children[word[i]]
            return  cur.endOfWord

        return dfs(self.root, word, 0)

