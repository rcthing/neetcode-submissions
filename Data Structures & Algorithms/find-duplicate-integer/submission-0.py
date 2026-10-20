class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0
        while True:
            s = nums[s]
            f = nums[f]
            f = nums[f]

            if f == s: break
        
        s2 = 0

        while True:
            s = nums[s]
            s2 = nums[s2]

            if s2 == s: break
        return s