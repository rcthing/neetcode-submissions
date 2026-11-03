class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = []
        for stone in stones:
            heapq.heappush(queue, -stone)

        while len(queue) > 1:
            s1 = -heapq.heappop(queue)
            s2 = -heapq.heappop(queue)
            s1 -= s2

            if s1:
                heapq.heappush(queue, -s1)
        if queue:
            return -queue[0]
        else:
            return 0


        

