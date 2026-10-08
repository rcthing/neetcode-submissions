class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        import heapq
        res = []
        h = []

        for i in range(k):
            heapq.heappush(h, (-nums[i], i))

        res.append(-h[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(h, (-nums[i], i))

            while h[0][1] <= i - k:
                heapq.heappop(h)

            res.append(-h[0][0]) 
        return res





        