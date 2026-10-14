class Solution:
    1,2,3,4,5,6
    2,3,4,5,6,1
    3,4,5,6,1,2
    4,5,6,1,2,3
    5,6,1,2,3,4
    6,1,2,3,4,5
    1,2,3,4,5,6
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[l] <= target < nums[m] or nums[m] <= nums[r] and not nums[m] < target <= nums[r]:
                r = m - 1
            else:
                l = m + 1 
        return -1
            
