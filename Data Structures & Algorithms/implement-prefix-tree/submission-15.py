class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                cur.children[word[i]] = Node()
                cur = cur.children[word[i]]
        cur.isEnd = True



    def search(self, word: str) -> bool:
        cur = self.root

        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]

        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]

        return True
        
        