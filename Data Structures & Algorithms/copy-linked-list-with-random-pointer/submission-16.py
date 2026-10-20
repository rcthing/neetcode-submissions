"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_map = {None: None}

        cur = head
        while cur:
            newnode = Node(cur.val)
            new_map[cur] = newnode
            cur = cur.next

        cur = head
        while cur:
            new = new_map[cur]
            new.random = new_map[cur.random]
            new.next = new_map[cur.next]
            cur = cur.next

        return new_map[head]


        