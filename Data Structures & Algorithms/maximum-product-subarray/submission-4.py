class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mmax = maxi = mini = nums[0]
        for i in range(1, len(nums)):
            temp = maxi
            maxi = max(nums[i] * maxi, nums[i],  nums[i] * mini)
            mini = min(nums[i] * temp, nums[i], nums[i] * mini)
            mmax = max(mmax, maxi)

        return mmax