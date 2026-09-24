class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1
        

        for i in range(len(nums)):
            if dp[i] == 0:
                return False
                
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = 1

        return True
        

