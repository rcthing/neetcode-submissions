# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1= head
        p2 = head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        curr = p1.next
        p1.next = None

        pre = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        first = head
        second = pre
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next =  tmp1
            first = tmp1
            second = tmp2
