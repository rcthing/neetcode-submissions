class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        maxi = 0

        for n in nums:
            cn = n
            if n - 1 not in elems:
                max_len = 1
                while n + max_len in elems:
                    max_len += 1
            
                maxi = max(max_len, maxi)
        return maxi
