# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        before = dummy

        first = head
        second = head
        counter = 0

        while second:
            second = second.next
            counter += 1
            prev = second
            group_start = first
            if counter == k:
                while counter > 0:
                    tmp = first.next
                    first.next = prev
                    prev = first
                    first = tmp
                    counter -= 1
                before.next = prev
                before = group_start

        return dummy.next

