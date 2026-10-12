class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mini = r

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / m)

            if hours > h:
                l = m + 1
            else:
                mini = min(mini, m)
                r = m - 1
        return mini

