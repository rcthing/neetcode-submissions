class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(node):
            while par[node] != node:
                node = par[node]
            return node

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[n2] = p1
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[n1] = p2
                par[p1] = p2
                rank[p2] += rank[p1]
            return True


        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]
            
