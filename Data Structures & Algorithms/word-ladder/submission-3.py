class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)

        adj = defaultdict(list)
        wordList.append(beginWord)

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                counter = 0
                for k in range(n):
                    if wordList[i][k] != wordList[j][k]:
                        counter += 1
                    if counter == 2:
                        break
                if counter == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        q = deque()
        q.append(beginWord)
        level = 1
        visited = set()

        while q:
            for _ in range(len(q)):
                n = q.popleft()
                visited.add(n)
                if n == endWord:
                    return level

                for ch in adj[n]:
                    if ch not in visited:
                        q.append(ch)
            level += 1
        return 0
