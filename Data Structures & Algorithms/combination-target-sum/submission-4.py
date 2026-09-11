class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(start_index, cur_sum, path):
            if cur_sum == target:
                ans.append(path[:])
                return
            elif cur_sum > target:
                return
            else:
                for i in range(start_index, len(nums)):
                    dfs(i, cur_sum + nums[i], path + [nums[i]])

        dfs(0, 0, [])
        return ans