# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        walker = dummy
        carry = 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val

            if l2:
                val += l2.val

            if val > 9:
                carry = 1
            else:
                carry = 0
            walker.next = ListNode(val % 10)
            walker = walker.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            walker.next = ListNode(1)

        return dummy.next



        