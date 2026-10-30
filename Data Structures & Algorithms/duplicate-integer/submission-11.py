class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = set(nums)
        return len(nums) != len(hmap)