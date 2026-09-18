class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}

        for word in words:
            for l in word:
                adj[l] = set()

        for i in range(len(words) - 1):
            j = 0
            if len(words[i]) > len(words[i+1]) and words[i][:len(words[i+1])] == words[i+1]:
                return ""
            
            while j < min(len(words[i]), len(words[i+1])) and words[i][j] == words[i+1][j]:
                j += 1

            if j < min(len(words[i]), len(words[i+1])):
                adj[words[i][j]].add(words[i+1][j])
                
        
        res = []
        visit = {}
        def dfs(l):
            if l in visit:
                return visit[l]

            visit[l] = True

            for n in adj[l]:
                if dfs(n):
                    return True

            visit[l] = False

            res.append(l)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
            