class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            s1 -= s2

            if s1:
                heapq.heappush(heap, -s1)
        if heap:
            return -heap[0]
        else:
            return 0


        

