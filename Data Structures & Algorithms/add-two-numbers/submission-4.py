# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = l1
        carry = 0
        while l1 and l2:
            if l1.val + l2.val + carry > 9:
                l1.val = (l1.val + l2.val + carry) % 10
                carry = 1
            else:
                l1.val = (l1.val + l2.val + carry)
                carry = 0
            prev = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            if l1.val + carry > 9:
                l1.val = (l1.val + carry) % 10
                carry = 1
            else:
                l1.val = l1.val + carry
                carry = 0
            prev = l1
            l1 = l1.next

        if l2:
            prev.next = l2
        while l2:
            if l2.val + carry > 9:
                l2.val = (l2.val + carry) % 10
                carry = 1
            else:
                l2.val = l2.val + carry
                carry = 0
            prev = l2
            l2 = l2.next

        if carry:
            prev.next = ListNode(1)

        return start



        