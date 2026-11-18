class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        adj = defaultdict(list)
        res = []

        for c, pre in prerequisites:
            adj[c].append(pre)

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for ch in adj[node]:
                if not dfs(ch):
                    return False
            res.append(node)
            cycle.discard(node)
            visited.add(node)
            adj[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        return res       


