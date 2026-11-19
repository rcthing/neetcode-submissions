class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            if node in visited:
                return 

            visited.add(node)
            for n in adj[node]:
                    dfs(n)
        dfs(0)
        if len(edges) != n - 1:
            return False
        return len(visited) == n
