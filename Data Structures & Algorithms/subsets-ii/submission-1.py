class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(start):
            res.append(subset.copy())
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                dfs(j+1)
                subset.pop()

        dfs(0)
        return res

            