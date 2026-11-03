class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.cnt = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.cnt, tweetId])
        self.cnt -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        maxHeap = []
        heapq.heapify(maxHeap)

        self.followMap[userId].add(userId)
        for followId in self.followMap[userId]:
            if followId in self.tweetMap:
                index = len(self.tweetMap[followId]) - 1
                count, tweetId = self.tweetMap[followId][index]
                heapq.heappush(maxHeap,[count, tweetId, followId, index - 1])
            
        while maxHeap and len(res) < 10:
            count, tweetId, followId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followId][index]
                heapq.heappush(maxHeap,[count, tweetId, followId, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
