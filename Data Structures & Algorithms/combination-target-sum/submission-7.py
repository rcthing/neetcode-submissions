class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(start_index, cur_sum, path):
            if cur_sum == target:
                ans.append(path.copy())
                return
            if start_index >= len(nums) or cur_sum > target:
                return
            else:
                path.append(nums[start_index])
                dfs(start_index, cur_sum + nums[start_index], path)
                path.pop()
                dfs(start_index+1, cur_sum, path)

        dfs(0, 0, [])
        return ans