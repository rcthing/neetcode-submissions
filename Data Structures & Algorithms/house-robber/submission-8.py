class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            maxi = max(a + n, b)
            a = b
            b = maxi

        return b