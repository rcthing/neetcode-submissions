# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        minheap = []
        #heapq.heapify(minheap)

        for k in range(len(lists)):
            if lists[k]:
                heapq.heappush(minheap, (lists[k].val, k))
        
        while minheap:
            val, index = heapq.heappop(minheap)
            prev.next = lists[index]
            prev = prev.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(minheap, (lists[index].val, index))
        return dummy.next

















        while True:
            mini = None
            index = -1
            for k in range (len(lists)):
                head = lists[k]
                if head:
                    if mini == None or head.val < mini:
                        mini = head.val
                        index = k
            if index == -1:
                break
            prev.next = lists[index]
            prev = prev.next
            lists[index] = lists[index].next
        return dummy.next


