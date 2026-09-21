class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mmax = maxi = mini = nums[0]
        for i in range(1, len(nums)):
            maxi, mini = max(nums[i] * maxi, nums[i],  nums[i] * mini), min(nums[i] * maxi, nums[i], nums[i] * mini)
            mmax = max(mmax, maxi)

        return mmax