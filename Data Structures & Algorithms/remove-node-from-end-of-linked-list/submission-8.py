# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head

        while n > 0:
            r = r.next
            n -= 1

        while r != None:
            r = r.next
            l = l.next

        nxt = l.next.next
        l.next = nxt
        
 
        return dummy.next