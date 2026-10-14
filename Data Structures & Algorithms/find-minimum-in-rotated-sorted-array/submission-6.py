class Solution:
    #1234567
    #2345671
    #3456712
    #4567123
    #5671234
    #6712345
    #7123456
    #1234567
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                if nums[r] < nums[l]:
                    l = m + 1
                else:
                    return nums[l]
            else:
                if nums[m - 1] < nums[m]:
                    r = m - 1
                else:
                    return nums[m]
        return nums[m]
