class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            if 0 > k:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1