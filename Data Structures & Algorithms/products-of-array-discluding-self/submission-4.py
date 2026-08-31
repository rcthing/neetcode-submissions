class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pre_prod = [0] * n
        suf_prod = [0] * n
        pre_prod[0] = 1
        suf_prod[n-1] = 1

        for i in range(1, n):
            pre_prod[i] = pre_prod[i-1] * nums[i-1]
            
        for i in range(n-2, -1, -1):
            suf_prod[i] = suf_prod[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = pre_prod[i] * suf_prod[i]
        
        return ans
            