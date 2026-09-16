"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}

        def dfs(cur):
            if cur in created:
                return created[cur]
            created[cur] = Node(cur.val)

            for n in cur.neighbors:
                created[cur].neighbors.append(dfs(n))
            return created[cur]

        if node:
            return dfs(node) 
        return None