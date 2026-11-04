class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        self.minHeap = []
        heapq.heapify(self.minHeap)
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) + 1 < len(self.minHeap):
            el = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -el)
        elif len(self.maxHeap) > len(self.minHeap):
            el = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, el)

        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
        