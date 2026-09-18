class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            c = nums[i]
            c = max(a + c, b)
            a = b
            b = c


        return c