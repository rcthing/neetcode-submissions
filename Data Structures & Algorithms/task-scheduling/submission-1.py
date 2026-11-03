class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        queue = deque()
        time = 0
        maxheap = []

        for count in freq:
            if count != 0:
                heapq.heappush(maxheap, -count)
        
        while maxheap or queue:
            if queue and queue[0][1] <= time:
                #print(queue)
                el = queue.popleft()
                heapq.heappush(maxheap, el[0])

            if not maxheap:
                time += 1
                #print("Idle")
            else:
                #print(list(maxheap))
                top = heapq.heappop(maxheap)
                top += 1
                if top:
                    queue.append([top, time + n + 1])
                time += 1
            
        return time