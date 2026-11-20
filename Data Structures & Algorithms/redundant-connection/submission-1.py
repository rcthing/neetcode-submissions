class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        adj = defaultdict(list)
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for ch in adj[node]:
                if ch != parent:
                    if dfs(ch, node) == False:
                        return False
            visited.discard(node)
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            if dfs(n1, -1) == False:
                return [n1,n2]
