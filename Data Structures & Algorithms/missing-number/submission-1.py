class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nr = 0
        for n in nums:
            nr += n

        return len(nums) * (len(nums)+1) // 2 - nr