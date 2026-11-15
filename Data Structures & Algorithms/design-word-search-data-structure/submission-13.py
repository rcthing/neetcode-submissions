class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        
        def dfs(i, cur):
            if i == len(word):
                return cur.isEnd

            if word[i] == ".":
                for key in cur.children:
                    if dfs(i+1, cur.children[key]):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                else:
                    return dfs(i+1, cur.children[word[i]])
        return dfs(0, self.root)

        
