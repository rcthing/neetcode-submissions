class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        seen = set()
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for n in nums:
                if n not in seen:
                    seen.add(n)
                    subset.append(n)
                    dfs()

                    seen.discard(n)
                    subset.pop()
        dfs()
        return res
            