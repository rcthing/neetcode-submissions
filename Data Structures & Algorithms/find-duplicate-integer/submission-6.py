class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if f == s: break
        
        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        return s