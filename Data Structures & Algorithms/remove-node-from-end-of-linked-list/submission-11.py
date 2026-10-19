# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        dummy = ListNode()
        dummy.next = head
        s = dummy
        
        while n:
            n -= 1
            p = p.next
        
        while p:
            s = s.next
            p = p.next
        
        if s and s.next:
            s.next = s.next.next

        return dummy.next
        
