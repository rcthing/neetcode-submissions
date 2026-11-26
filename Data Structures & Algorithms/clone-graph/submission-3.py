"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        root = node
        newold = {}

        def dfs(node):
            if node in newold:
                return
                
            newold[node] = Node(node.val)
            
            for n in node.neighbors:
                dfs(n)

        dfs(root)
        
        for n in newold:
            for nei in n.neighbors:
                newold[n].neighbors.append(newold[nei])
        
        return newold[root]