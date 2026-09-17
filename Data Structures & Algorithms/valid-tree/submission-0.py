class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodesEdges = {i:[] for i in range(n)}

        for p in edges:
            nodesEdges[p[0]].append(p[1])
            nodesEdges[p[1]].append(p[0])

        path = set()

        def dfs(node, parent):
            if node in path:
                return False

            path.add(node)

            for neighbour in nodesEdges[node]:
                if neighbour != parent:
                    if not dfs(neighbour, node):
                        return False

            return True

        if not dfs(0,0):
            return False

        if len(path) != n:
            return False

        return True

