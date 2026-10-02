class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        maxi = 0

        for n in nums:
            count = 1
            if n-1 not in hset:
                cn = n
                while cn+1 in hset:
                    cn += 1
                    count += 1
                maxi = max(count,maxi)

        return maxi