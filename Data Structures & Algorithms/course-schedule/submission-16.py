class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        def dfs(node):
            if node in visited:
                return False
            elif adj[node] == []:
                return True
            
            visited.add(node)
            for children in adj[node]:
                if not dfs(children):
                    return False
            visited.discard(node)
            adj[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True