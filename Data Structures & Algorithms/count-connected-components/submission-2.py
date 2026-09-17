class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nEdges = {i:[] for i in range(n)}
        
        for e in edges:
            nEdges[e[0]].append(e[1])
            nEdges[e[1]].append(e[0])

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return

            visited.add(node)

            for ne in nEdges[node]:
                if ne != parent:
                    dfs(ne, node)
            return
        
        dfs(0,0)
        c = 1

        for node in range(n):
            if node not in visited:
                dfs(node,node)
                c += 1

        return c

                