class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for cord in points:
            d = cord[0]**2 + cord[1]**2
            heapq.heappush(heap, (-d, cord))
            if len(heap) > k:
                heapq.heappop(heap)

        return [cord for d,cord in heap]