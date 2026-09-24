class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        maxi = nums[0]

        for i in range(len(nums)-1, -1, -1):
            curent = max(nums[i], prev + nums[i])
            maxi = max(curent, maxi)
            prev = curent

        return maxi
