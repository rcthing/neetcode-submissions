class Solution:
    def findMin(self, nums: List[int]) -> int:
        lg = len(nums)
        l = 0
        r = lg - 1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
