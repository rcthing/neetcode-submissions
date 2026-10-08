class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        res = []
        q = deque()
        i = 0

        while i < len(nums):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
            i += 1
        return res
