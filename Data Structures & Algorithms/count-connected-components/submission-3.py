class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        counter = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            
            for n in adj[node]:
                dfs(n)
            
            return
        
        for node in range(n):
            if node not in visited:
                counter += 1
                dfs(node)
        return counter

