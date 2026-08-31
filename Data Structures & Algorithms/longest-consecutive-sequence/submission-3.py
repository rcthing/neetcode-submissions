class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        maxi = 0

        for n in nums:
            max_len = 1
            cn = n
            if cn-1 not in elems:
                while cn + 1 in elems:
                    cn += 1
                    max_len += 1
            
            if max_len > maxi:
                maxi = max_len
        return maxi
