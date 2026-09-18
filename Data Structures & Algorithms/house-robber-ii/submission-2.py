class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = b = 0
        for i in range(len(nums)-1):
            maxi1 = max(a + nums[i], b)
            a = b
            b = maxi1

        a = b = maxi2 = 0
        for i in range(1, len(nums)):
            maxi2 = max(a + nums[i], b)
            a = b
            b = maxi2

        return max(maxi1,maxi2)