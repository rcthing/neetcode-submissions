class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.val_map = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from list
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    # insert at right
    def insert(self, node):
        last = self.right.prev
        last.next, self.right.prev, node.next, node.prev = node, node, self.right, last

    def get(self, key: int) -> int:
        if key in self.val_map:
            self.remove(self.val_map[key])
            self.insert(self.val_map[key])
            return self.val_map[key].val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.val_map:
            self.val_map[key].val = value
            self.remove(self.val_map[key])
            self.insert(self.val_map[key])
        else:
            self.cap -= 1
            if self.cap < 0:
                self.cap += 1
                del self.val_map[self.left.next.key]
                self.remove(self.left.next)
                
            new = Node(key,value)
            self.insert(new)
            self.val_map[key] = new


        
