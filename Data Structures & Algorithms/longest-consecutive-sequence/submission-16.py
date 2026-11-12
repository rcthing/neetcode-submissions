class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        maxi = 0

        for n in nums:
            if n-1 not in hset:
                count = 1
                while n + count in hset:
                    count += 1
                maxi = max(count,maxi)

        return maxi