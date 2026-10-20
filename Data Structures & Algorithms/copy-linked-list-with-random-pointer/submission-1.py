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
        dummy = Node(0)
        prev = dummy
        old_to_new = {}
        cur = head
        while cur:
            newnode = Node(cur.val)
            prev.next = newnode
            old_to_new[cur] = newnode
            prev = prev.next
            cur = cur.next

        cur = head
        while cur:
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            else:
                old_to_new[cur].random = None
            cur = cur.next

        return dummy.next


        