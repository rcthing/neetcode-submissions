class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [0] * n
        pre_prod[0] = 1
        suf_prod = 1

        for i in range(1, n):
            pre_prod[i] = pre_prod[i-1] * nums[i-1]
            
        for i in range(n-1, -1, -1):
            pre_prod[i] *= suf_prod
            suf_prod *= nums[i]
        
        return pre_prod
            